"""Small graph container for early papercone experiments."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

from papercone.core.models import Paper, PaperEdge


EndpointRole = Literal["source", "target"]


@dataclass(frozen=True, slots=True)
class MissingEdgeEndpoint:
    """A validation issue for an edge that points outside the local graph."""

    edge_index: int
    paper_id: str
    role: EndpointRole


class GraphValidationError(ValueError):
    """Raised when a graph snapshot has invalid internal references."""


@dataclass(slots=True)
class PaperGraph:
    """A local graph snapshot around one or more seed papers."""

    papers: dict[str, Paper] = field(default_factory=dict)
    edges: list[PaperEdge] = field(default_factory=list)

    def add_paper(self, paper: Paper) -> None:
        self.papers[paper.id] = paper

    def add_edge(self, edge: PaperEdge) -> None:
        self.edges.append(edge)

    def paper_count(self) -> int:
        return len(self.papers)

    def edge_count(self) -> int:
        return len(self.edges)

    def missing_edge_endpoints(self) -> tuple[MissingEdgeEndpoint, ...]:
        """Return edge endpoints that do not exist in ``papers``."""

        missing: list[MissingEdgeEndpoint] = []
        for index, edge in enumerate(self.edges):
            if edge.source_id not in self.papers:
                missing.append(
                    MissingEdgeEndpoint(edge_index=index, paper_id=edge.source_id, role="source")
                )
            if edge.target_id not in self.papers:
                missing.append(
                    MissingEdgeEndpoint(edge_index=index, paper_id=edge.target_id, role="target")
                )
        return tuple(missing)

    def validate(self) -> None:
        """Raise ``GraphValidationError`` if an edge endpoint is missing."""

        missing = self.missing_edge_endpoints()
        if not missing:
            return

        details = ", ".join(
            f"edge[{issue.edge_index}].{issue.role}_id={issue.paper_id!r}"
            for issue in missing
        )
        raise GraphValidationError(f"Missing edge endpoints: {details}")
