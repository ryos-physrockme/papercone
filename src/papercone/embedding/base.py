from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol


Vector = tuple[float, ...]
Point2D = tuple[float, float]


class TextEmbedder(Protocol):
    def embed_texts(self, texts: Sequence[str]) -> list[Vector]:
        pass


class Projector2D(Protocol):
    def project(self, vectors: Sequence[Vector]) -> list[Point2D]:
        pass
