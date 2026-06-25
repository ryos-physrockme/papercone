# Cycle 1: domain model

Goal: establish the smallest useful paper graph model.

## User/developer experience

A developer can create a seed paper, references, and citations as local Python objects, then export a graph-shaped payload for later visualization.

## Current scope

Implemented in the initial scaffold:

- `Paper`
- `PaperEdge`
- `PaperGraph`
- demo graph fixture
- graph-to-dict export helper
- coordinate sketch
- provider protocol sketch

## Next refinements

- Add stable identifier handling for arXiv, DOI, INSPIRE, OpenAlex, and Semantic Scholar IDs.
- Add JSON serialization that preserves tuples as lists and can round-trip.
- Add edge direction conventions for rendering past-to-future citation lines.
- Add validation for missing edge endpoints.
- Add a CLI command that writes `examples/demo_graph.json` from the Python fixture.
