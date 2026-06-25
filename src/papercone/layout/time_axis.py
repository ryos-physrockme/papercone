"""Helpers for converting publication metadata into a time axis."""

from __future__ import annotations

from papercone.core.models import Paper


def year_to_z(paper: Paper) -> float | None:
    """Use publication year as the first z-axis convention."""

    if paper.year is None:
        return None
    return float(paper.year)
