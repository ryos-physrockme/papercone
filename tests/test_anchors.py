from papercone.anchors.models import Anchor


def test_anchor_model_for_personal_note() -> None:
    anchor = Anchor(
        id="note-ai-integrability",
        kind="note",
        title="AI-assisted integrability search",
        text="Explore Lax-pair and non-integrability checks with CAS-backed agents.",
        tags=("integrability", "ai-for-science"),
    )

    assert anchor.kind == "note"
    assert "integrability" in anchor.tags
