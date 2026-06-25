"""Static layout helpers used before semantic projection exists."""

from __future__ import annotations

from papercone.core.coordinates import PaperCoordinate
from papercone.core.graph import PaperGraph
from papercone.layout.time_axis import year_to_z


def simple_line_layout(graph: PaperGraph) -> list[PaperCoordinate]:
    """Place papers on a simple deterministic line for early visualization."""

    coordinates: list[PaperCoordinate] = []
    for index, paper in enumerate(graph.papers.values()):
        z = year_to_z(paper)
        coordinates.append(
            PaperCoordinate(
                paper_id=paper.id,
                x=float(index),
                y=0.0,
                z=0.0 if z is None else z,
            )
        )
    return coordinates
