"""Provider-agnostic domain models for local papercone graph snapshots."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


ExternalIdKind = Literal["arxiv", "doi", "inspire", "openalex", "semantic_scholar"]
EdgeKind = Literal["cites", "cited_by", "related"]


@dataclass(frozen=True, slots=True)
class ExternalId:
    """A normalized external identifier for a scholarly work."""

    kind: ExternalIdKind
    value: str


@dataclass(frozen=True, slots=True)
class Paper:
    """A scholarly work in a local papercone graph snapshot."""

    id: str
    title: str
    abstract: str | None = None
    year: int | None = None
    publication_date: str | None = None
    venue: str | None = None
    authors: tuple[str, ...] = field(default_factory=tuple)
    source: str = "unknown"
    citation_count: int | None = None
    external_ids: tuple[ExternalId, ...] = field(default_factory=tuple)

    def external_id(self, kind: ExternalIdKind) -> str | None:
        """Return the first external identifier value for ``kind``, if present."""

        for external_id in self.external_ids:
            if external_id.kind == kind:
                return external_id.value
        return None


@dataclass(frozen=True, slots=True)
class PaperEdge:
    """A directed relation between two papers.

    Direction convention:
    - ``cites`` means ``source_id`` cites ``target_id``.
    - ``cited_by`` means ``source_id`` is cited by ``target_id``.
    - ``related`` is an undirected-looking relation stored with explicit endpoints.
    """

    source_id: str
    target_id: str
    kind: EdgeKind
