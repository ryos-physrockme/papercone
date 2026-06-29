"""JSON helpers for graph snapshots."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

from papercone.core.export import graph_to_dict
from papercone.core.graph import PaperGraph
from papercone.core.models import EdgeKind, ExternalId, ExternalIdKind, Paper, PaperEdge


def write_graph_json(graph: PaperGraph, path: str | Path) -> None:
    """Write a graph snapshot to a JSON file."""

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload: dict[str, list[dict[str, Any]]] = graph_to_dict(graph)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def read_graph_json(path: str | Path) -> PaperGraph:
    """Read a graph snapshot from a JSON file."""

    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return graph_from_dict(payload)


def graph_from_dict(payload: dict[str, Any]) -> PaperGraph:
    """Build a ``PaperGraph`` from a JSON-compatible payload.

    Unknown paper fields, such as render-only ``x``, ``y``, and ``z`` coordinates,
    are ignored so that visualization snapshots can still be loaded as graphs.
    """

    graph = PaperGraph()
    for paper_payload in payload.get("papers", []):
        graph.add_paper(_paper_from_dict(paper_payload))
    for edge_payload in payload.get("edges", []):
        graph.add_edge(_edge_from_dict(edge_payload))
    return graph


def _paper_from_dict(payload: dict[str, Any]) -> Paper:
    external_ids = tuple(_external_id_from_dict(item) for item in payload.get("external_ids", []))
    return Paper(
        id=payload["id"],
        title=payload["title"],
        abstract=payload.get("abstract"),
        year=payload.get("year"),
        publication_date=payload.get("publication_date"),
        venue=payload.get("venue"),
        authors=tuple(payload.get("authors", ())),
        source=payload.get("source", "unknown"),
        citation_count=payload.get("citation_count"),
        external_ids=external_ids,
    )


def _external_id_from_dict(payload: dict[str, Any]) -> ExternalId:
    return ExternalId(
        kind=cast(ExternalIdKind, payload["kind"]),
        value=payload["value"],
    )


def _edge_from_dict(payload: dict[str, Any]) -> PaperEdge:
    return PaperEdge(
        source_id=payload["source_id"],
        target_id=payload["target_id"],
        kind=cast(EdgeKind, payload["kind"]),
    )
