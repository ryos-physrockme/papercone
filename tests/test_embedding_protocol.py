from collections.abc import Sequence

from papercone.embedding.base import Point2D, Projector2D, TextEmbedder, Vector


class LengthEmbedder:
    def embed_texts(self, texts: Sequence[str]) -> list[Vector]:
        return [(float(len(text)),) for text in texts]


class FirstTwoProjector:
    def project(self, vectors: Sequence[Vector]) -> list[Point2D]:
        return [(vector[0], 0.0) for vector in vectors]


def test_embedding_and_projection_protocols() -> None:
    embedder: TextEmbedder = LengthEmbedder()
    projector: Projector2D = FirstTwoProjector()

    vectors = embedder.embed_texts(["abc"])
    points = projector.project(vectors)

    assert vectors == [(3.0,)]
    assert points == [(3.0, 0.0)]
