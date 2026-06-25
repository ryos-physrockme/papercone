"""Personal research anchors."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


AnchorKind = Literal["own_paper", "saved_paper", "note", "draft", "query"]


@dataclass(frozen=True, slots=True)
class Anchor:
    """A user-defined position to place on the papercone map."""

    id: str
    kind: AnchorKind
    title: str
    text: str
    tags: tuple[str, ...] = field(default_factory=tuple)
    linked_paper_id: str | None = None
