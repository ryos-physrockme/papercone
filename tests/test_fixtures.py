from papercone.core.fixtures import make_demo_graph


def test_demo_graph_shape() -> None:
    graph = make_demo_graph()

    assert graph.paper_count() == 3
    assert graph.edge_count() == 2
