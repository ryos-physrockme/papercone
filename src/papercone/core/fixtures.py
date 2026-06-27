"""Tiny fixtures used by examples and early tests."""

from __future__ import annotations

from papercone.core.graph import PaperGraph
from papercone.core.models import ExternalId, Paper, PaperEdge


def make_demo_graph() -> PaperGraph:
    """Create a minimal hand-written citation cone.

    The IDs are placeholders. Cycle 2 will replace this with provider data.
    """

    graph = PaperGraph()
    graph.add_paper(
        Paper(
            id="seed",
            title="Seed paper",
            abstract="The paper at the center of the local research map.",
            year=2024,
            publication_date="2024-01-01",
            source="fixture",
            external_ids=(ExternalId(kind="arxiv", value="2401.00001"),),
        )
    )
    graph.add_paper(
        Paper(
            id="reference",
            title="Reference paper",
            abstract="A past work cited by the seed paper.",
            year=2019,
            publication_date="2019-01-01",
            source="fixture",
            external_ids=(ExternalId(kind="doi", value="10.0000/reference"),),
        )
    )
    graph.add_paper(
        Paper(
            id="citation",
            title="Future citation paper",
            abstract="A later work that cites the seed paper.",
            year=2026,
            publication_date="2026-01-01",
            source="fixture",
            external_ids=(ExternalId(kind="openalex", value="W0000000001"),),
        )
    )
    graph.add_edge(PaperEdge(source_id="seed", target_id="reference", kind="cites"))
    graph.add_edge(PaperEdge(source_id="seed", target_id="citation", kind="cited_by"))
    return graph
