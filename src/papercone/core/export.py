"""Export helpers for local graph snapshots."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from papercone.core.graph import PaperGraph


def graph_to_dict(graph: PaperGraph) -> dict[str, list[dict[str, Any]]]:
    """Convert a paper graph to a JSON-serializable dictionary."""

    return {
        "papers": [asdict(paper) for paper in graph.papers.values()],
        "edges": [asdict(edge) for edge in graph.edges],
    }
