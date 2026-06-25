# Roadmap

papercone is developed as a sequence of small, experience-driven cycles. Each pull request should add one observable capability.

## Cycle 0: scaffold

Status: initial repository scaffold.

Goal: make the repository understandable and testable before feature work starts.

Deliverables:

- README
- product vision
- roadmap
- architecture note
- minimal Python package
- smoke test

## Cycle 1: domain model

Experience: a seed paper and a small mock citation cone can be represented and exported.

Deliverables:

- `Paper`
- `PaperEdge`
- `PaperGraph`
- fixture data
- JSON export
- tests for graph construction

## Cycle 2: provider integration

Experience: a real seed paper can be fetched from a scholarly data provider.

Initial provider preference:

1. INSPIRE for high-energy physics workflows.
2. OpenAlex for broad metadata and topics.
3. Semantic Scholar for embeddings and recommendations where useful.

Deliverables:

- provider protocol
- first provider implementation
- local cache
- CLI command to fetch one-hop data

## Cycle 3: static papercone view

Experience: a browser view displays a time-aware citation cone.

Deliverables:

- demo graph JSON
- frontend scaffold
- 3D node and edge rendering
- hover panel for paper metadata

## Cycle 4: semantic x-y layout

Experience: papers with similar content appear close together in the x-y plane.

Deliverables:

- embedding interface
- projection interface
- PCA-based projection
- graph export with x, y, z coordinates

## Cycle 5: personal anchors

Experience: own papers, notes, drafts, and saved papers appear as map pins.

Deliverables:

- anchor model
- anchor store
- anchor embedding
- anchor rendering

## Cycle 6: query jump

Experience: a free-form research query jumps to a semantic location on the map.

Deliverables:

- query embedding
- nearest-neighbor search
- frontend search box
- camera transition to target region

## Cycle 7: frontier scoring

Experience: growing or underexplored regions are highlighted.

Initial score components:

- recency
- citation velocity
- cluster growth
- bridge score
- semantic novelty
- personal relevance

## Cycle 8: path finding

Experience: the system suggests a reading path from a personal anchor to a frontier paper or cluster.

Deliverables:

- weighted graph search
- path explanation
- path rendering on the map
