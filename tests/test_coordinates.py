from papercone.core.coordinates import PaperCoordinate


def test_coordinate_keeps_visual_axes() -> None:
    coord = PaperCoordinate(paper_id="seed", x=0.0, y=1.0, z=2026.0)

    assert coord.paper_id == "seed"
    assert coord.z == 2026.0
