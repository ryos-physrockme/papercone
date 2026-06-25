from papercone.core.models import Paper
from papercone.layout.time_axis import year_to_z


def test_year_to_z_uses_publication_year() -> None:
    assert year_to_z(Paper(id="seed", title="Seed", year=2026)) == 2026.0


def test_year_to_z_handles_missing_year() -> None:
    assert year_to_z(Paper(id="seed", title="Seed")) is None
