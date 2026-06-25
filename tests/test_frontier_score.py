from papercone.scoring.frontier import FrontierScore


def test_frontier_score_total_is_decomposed() -> None:
    score = FrontierScore(
        paper_id="seed",
        recency=1.0,
        citation_velocity=2.0,
        bridge=0.5,
        saturation_penalty=0.25,
    )

    assert score.total == 3.25
