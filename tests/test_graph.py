from papercone.core.graph import PaperGraph
from papercone.core.models import Paper, PaperEdge


def test_graph_counts_papers_and_edges() -> None:
    graph = PaperGraph()
    graph.add_paper(Paper(id="paper-a", title="A"))
    graph.add_paper(Paper(id="paper-b", title="B"))
    graph.add_edge(PaperEdge(source_id="paper-b", target_id="paper-a", kind="cites"))

    assert graph.paper_count() == 2
    assert graph.edge_count() == 1
