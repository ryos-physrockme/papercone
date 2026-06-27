from papercone.core.models import ExternalId, Paper, PaperEdge


def test_paper_model_minimal_fields() -> None:
    paper = Paper(id="arxiv:2305.01421", title="Model building by coset space dimensional reduction")

    assert paper.id == "arxiv:2305.01421"
    assert paper.title.startswith("Model building")
    assert paper.source == "unknown"


def test_paper_model_keeps_normalized_external_ids() -> None:
    paper = Paper(
        id="csdr-8d",
        title="Model building by coset space dimensional reduction",
        external_ids=(
            ExternalId(kind="arxiv", value="2305.01421"),
            ExternalId(kind="inspire", value="2655085"),
        ),
    )

    assert paper.external_id("arxiv") == "2305.01421"
    assert paper.external_id("doi") is None


def test_paper_edge_kind() -> None:
    edge = PaperEdge(source_id="new", target_id="old", kind="cites")

    assert edge.source_id == "new"
    assert edge.target_id == "old"
    assert edge.kind == "cites"
