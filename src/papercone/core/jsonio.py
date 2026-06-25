"""JSON helpers for graph snapshots."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from papercone.core.export import graph_to_dict
from papercone.core.graph import PaperGraph


def write_graph_json(graph: PaperGraph, path: str | Path) -> None:
    """Write a graph snapshot to a JSON file."""

    payload: dict[str, list[dict[str, Any]]] = graph_to_dict(graph)
    Path(path).write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
