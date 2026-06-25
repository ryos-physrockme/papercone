"""Provider protocol for scholarly data sources."""

from __future__ import annotations

from typing import Protocol

from papercone.core.models import Paper, PaperEdge


class PaperProvider(Protocol):
    """Minimal interface implemented by scholarly data providers."""

    def fetch_paper(self, paper_id: str) -> Paper:
        """Fetch one paper by a provider-specific or normalized identifier."""
        ...

    def fetch_references(self, paper_id: str) -> list[PaperEdge]:
        """Fetch edges from the paper to works it cites."""
        ...

    def fetch_citations(self, paper_id: str) -> list[PaperEdge]:
        """Fetch edges from the paper to works that cite it."""
        ...
