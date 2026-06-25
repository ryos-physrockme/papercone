# Product vision

papercone is a personal research map for moving from a researcher's current position to possible frontiers.

It combines citation graph structure, semantic embeddings, time-aware visualization, and user-defined anchors. The product should help answer questions like:

- Where is my current work located inside the literature?
- Which nearby clusters are growing quickly?
- Which distant clusters are connected by a plausible reading path?
- Which interdisciplinary gaps look reachable from my background?
- What should I read next if I want to move toward a target frontier?

## Non-goals for the first milestone

- It is not a full-text PDF parser.
- It is not a generic reference manager.
- It is not an LLM-only research recommender.
- It is not trying to replace arXiv, INSPIRE, OpenAlex, Semantic Scholar, Zotero, or Connected Papers.

The first product value is a map-like research navigation experience built on top of existing scholarly data providers.

## North-star interaction

1. The user enters one or more seed papers.
2. papercone expands a local citation cone.
3. The map places papers by semantic similarity in x-y and publication time in z.
4. The user's own papers, notes, drafts, and queries appear as anchors.
5. The system highlights frontier-like regions and suggests paths from the user's anchors.
