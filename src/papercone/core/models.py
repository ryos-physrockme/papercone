"""Initial domain model sketches.

These objects are intentionally small. Cycle 1 will expand them into the tested
paper graph model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


EdgeKind = Literal["cites", "cited_by", "related"]


@dataclass(frozen=True, slots=True)
class Paper:
    """A scholarly work in a local papercone graph snapshot."""

    id: str
    title: str
    abstract: str | None = None
    year: int | None = None
    authors: tuple[str, ...] = field(default_factory=tuple)
    source: str = "unknown"
    citation_count: int | None = None


@dataclass(frozen=True, slots=True)
class PaperEdge:
    """A directed relation between two papers."""

    source_id: str
    target_id: str
    kind: EdgeKind
