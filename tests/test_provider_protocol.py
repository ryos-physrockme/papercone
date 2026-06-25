from papercone.core.models import Paper, PaperEdge
from papercone.providers.base import PaperProvider


class FakeProvider:
    def fetch_paper(self, paper_id: str) -> Paper:
        return Paper(id=paper_id, title="Fake paper", source="fake")

    def fetch_references(self, paper_id: str) -> list[PaperEdge]:
        return [PaperEdge(source_id=paper_id, target_id="reference", kind="cites")]

    def fetch_citations(self, paper_id: str) -> list[PaperEdge]:
        return [PaperEdge(source_id=paper_id, target_id="citation", kind="cited_by")]


def test_fake_provider_matches_protocol() -> None:
    provider: PaperProvider = FakeProvider()

    assert provider.fetch_paper("seed").id == "seed"
    assert provider.fetch_references("seed")[0].kind == "cites"
    assert provider.fetch_citations("seed")[0].kind == "cited_by"
