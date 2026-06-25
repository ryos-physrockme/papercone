"""Coordinate objects for map-ready graph data."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PaperCoordinate:
    """A paper position in the papercone visualization space."""

    paper_id: str
    x: float
    y: float
    z: float
