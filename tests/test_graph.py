import pytest

from papercone.core.graph import GraphValidationError, PaperGraph
from papercone.core.models import Paper, PaperEdge


def test_graph_counts_papers_and_edges() -> None:
    graph = PaperGraph()
    graph.add_paper(Paper(id="paper-a", title="A"))
    graph.add_paper(Paper(id="paper-b", title="B"))
    graph.add_edge(PaperEdge(source_id="paper-b", target_id="paper-a", kind="cites"))

    assert graph.paper_count() == 2
    assert graph.edge_count() == 1


def test_graph_validate_accepts_known_edge_endpoints() -> None:
    graph = PaperGraph()
    graph.add_paper(Paper(id="seed", title="Seed"))
    graph.add_paper(Paper(id="reference", title="Reference"))
    graph.add_edge(PaperEdge(source_id="seed", target_id="reference", kind="cites"))

    graph.validate()


def test_graph_validate_reports_missing_edge_endpoints() -> None:
    graph = PaperGraph()
    graph.add_paper(Paper(id="seed", title="Seed"))
    graph.add_edge(PaperEdge(source_id="seed", target_id="missing", kind="cites"))

    missing = graph.missing_edge_endpoints()

    assert len(missing) == 1
    assert missing[0].paper_id == "missing"
    assert missing[0].role == "target"
    with pytest.raises(GraphValidationError, match="missing"):
        graph.validate()
