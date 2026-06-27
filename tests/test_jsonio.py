import json

from papercone.core.fixtures import make_demo_graph
from papercone.core.graph import PaperGraph
from papercone.core.jsonio import graph_from_dict, read_graph_json, write_graph_json
from papercone.core.models import ExternalId, Paper, PaperEdge


def test_write_graph_json(tmp_path) -> None:
    path = tmp_path / "graph.json"

    write_graph_json(make_demo_graph(), path)

    payload = json.loads(path.read_text(encoding="utf-8"))
    assert len(payload["papers"]) == 3
    assert len(payload["edges"]) == 2


def test_read_graph_json_round_trips_core_fields(tmp_path) -> None:
    graph = PaperGraph()
    graph.add_paper(
        Paper(
            id="seed",
            title="Seed",
            authors=("A. Author",),
            external_ids=(ExternalId(kind="arxiv", value="2401.00001"),),
        )
    )
    graph.add_paper(Paper(id="reference", title="Reference"))
    graph.add_edge(PaperEdge(source_id="seed", target_id="reference", kind="cites"))
    path = tmp_path / "graph.json"

    write_graph_json(graph, path)
    restored = read_graph_json(path)

    assert restored.paper_count() == 2
    assert restored.edge_count() == 1
    assert restored.papers["seed"].authors == ("A. Author",)
    assert restored.papers["seed"].external_id("arxiv") == "2401.00001"
    restored.validate()


def test_graph_from_dict_ignores_visual_coordinates() -> None:
    payload = {
        "papers": [
            {
                "id": "seed",
                "title": "Seed",
                "year": 2026,
                "x": 0.1,
                "y": 0.2,
                "z": 2026,
            }
        ],
        "edges": [],
    }

    graph = graph_from_dict(payload)

    assert graph.papers["seed"].year == 2026
