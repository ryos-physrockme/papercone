"""Embedding and projection protocols."""

from __future__ import annotations

from typing import Protocol, Sequence


Vector = tuple[float, ...]
Point2D = tuple[float, float]


class TextEmbedder(Protocol):
    """Turn text into a vector representation."""

    def embed_texts(self, texts: Sequence[str]) -> list[Vector]:
        """Embed a batch of texts."""
        ...


class Projector2D(Protocol):
    """Project vectors to a two-dimensional map plane."""

    def project(self, vectors: Sequence[Vector]) -> list[Point2D]:
        """Project vectors to x-y coordinates."""
        ...
