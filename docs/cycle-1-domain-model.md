# Cycle 1: domain model

Goal: establish the smallest useful paper graph model.

## User/developer experience

A developer can create a seed paper, references, and citations as local Python objects, validate the graph, export it as JSON, and read it back without losing core metadata.

## Scope completed by this cycle

- `Paper`
- `ExternalId`
- `PaperEdge`
- `PaperGraph`
- edge endpoint validation
- demo graph fixture
- graph-to-dict export helper
- JSON write/read round-trip helpers
- coordinate sketch
- provider protocol sketch
- CLI command that writes a demo graph snapshot

## Direction convention

- `cites`: `source_id` cites `target_id`.
- `cited_by`: `source_id` is cited by `target_id`.
- `related`: explicit endpoints are preserved, but the relation should not yet be treated as causal.

This convention keeps provider data inspectable before the visualization layer decides how to draw past-to-future lines.

## Still later

- provider-specific normalization logic
- cache layout
- real one-hop provider expansion
- semantic projection
- frontend rendering
