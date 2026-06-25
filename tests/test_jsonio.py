import json

from papercone.core.fixtures import make_demo_graph
from papercone.core.jsonio import write_graph_json


def test_write_graph_json(tmp_path) -> None:
    path = tmp_path / "graph.json"

    write_graph_json(make_demo_graph(), path)

    payload = json.loads(path.read_text(encoding="utf-8"))
    assert len(payload["papers"]) == 3
    assert len(payload["edges"]) == 2
