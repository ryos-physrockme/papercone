from papercone.core.export import graph_to_dict
from papercone.core.fixtures import make_demo_graph


def test_graph_to_dict_is_json_shape() -> None:
    payload = graph_to_dict(make_demo_graph())

    assert sorted(payload) == ["edges", "papers"]
    assert len(payload["papers"]) == 3
    assert len(payload["edges"]) == 2
