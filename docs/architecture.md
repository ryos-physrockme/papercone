# Architecture

papercone is organized around a small core model and replaceable adapters.

## Conceptual layers

```text
user anchors + queries
        |
        v
semantic embedding and projection
        |
        v
paper graph: papers, edges, clusters, paths
        |
        v
providers: INSPIRE, OpenAlex, Semantic Scholar, local files
        |
        v
visualization: time-aware citation cone
```

## Core objects

### Paper

A scholarly work with stable identifiers and metadata.

Expected fields:

- id
- title
- abstract
- authors
- year
- publication_date
- venue
- source
- citation_count
- external_ids

### PaperEdge

A directed relation between papers.

Initial edge kinds:

- `cites`: source paper cites target paper
- `cited_by`: source paper is cited by target paper
- `related`: provider-supplied or embedding-derived relation

Internally, citation edges should preserve direction. A later visualization can choose whether to draw all edges from past to future.

### PaperGraph

A local graph snapshot around one or more seed papers.

Responsibilities:

- store papers and edges
- validate that edge endpoints exist when desired
- export to JSON
- eventually compute neighborhoods, clusters, scores, and paths

### Anchor

A user-defined position on the research map.

Anchor kinds:

- own paper
- saved paper
- note
- draft
- query

Anchors should eventually share the same embedding space as papers.

## Provider layer

Providers fetch metadata and graph edges from external scholarly data sources.

The provider interface should avoid leaking provider-specific response formats into the core model.

Initial protocol sketch:

```python
class PaperProvider(Protocol):
    def fetch_paper(self, paper_id: str) -> Paper: ...
    def fetch_references(self, paper_id: str) -> list[PaperEdge]: ...
    def fetch_citations(self, paper_id: str) -> list[PaperEdge]: ...
```

## Storage

The first storage target is plain JSON plus a small local cache. This keeps early development inspectable.

Possible later targets:

- SQLite for local persistence
- DuckDB and Parquet for larger offline snapshots
- vector index for embeddings
- graph database only if graph traversal becomes the bottleneck

## Visualization model

A renderable graph should contain enough data to draw a map without re-running provider calls.

Initial coordinate convention:

- `x`: semantic projection dimension 1
- `y`: semantic projection dimension 2
- `z`: publication time

Before semantic projection exists, x and y may be fixture coordinates.
