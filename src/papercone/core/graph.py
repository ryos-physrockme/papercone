"""Small graph container for early papercone experiments."""

from __future__ import annotations

from dataclasses import dataclass, field

from papercone.core.models import Paper, PaperEdge


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
