"""Initial frontier score data structure."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FrontierScore:
    """A decomposed frontier score for inspection and debugging."""

    paper_id: str
    recency: float = 0.0
    citation_velocity: float = 0.0
    cluster_growth: float = 0.0
    bridge: float = 0.0
    semantic_novelty: float = 0.0
    personal_relevance: float = 0.0
    saturation_penalty: float = 0.0

    @property
    def total(self) -> float:
        return (
            self.recency
            + self.citation_velocity
            + self.cluster_growth
            + self.bridge
            + self.semantic_novelty
            + self.personal_relevance
            - self.saturation_penalty
        )
