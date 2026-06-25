from papercone.core.fixtures import make_demo_graph
from papercone.layout.static import simple_line_layout


def test_simple_line_layout_returns_one_coordinate_per_paper() -> None:
    graph = make_demo_graph()
    coordinates = simple_line_layout(graph)

    assert len(coordinates) == graph.paper_count()
    assert {coord.paper_id for coord in coordinates} == set(graph.papers)
