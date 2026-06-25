# Development principles

## One pull request, one experience

Each pull request should make one new behavior visible to a user or developer.

Good PR shapes:

- "A seed paper can be represented as a graph node."
- "A one-hop citation cone can be exported as JSON."
- "A demo graph can be rendered in 3D."
- "A personal note can be placed on the map."

Avoid PRs that only say:

- "Refactor everything."
- "Add all providers."
- "Implement the research recommender."

## Keep the core small

The core package should define stable concepts: papers, edges, graphs, anchors, coordinates, scores, and paths.

Provider-specific APIs, visualization libraries, and embedding services should stay behind adapters.

## Prefer inspectable artifacts

Early outputs should be JSON files, small fixtures, and simple command-line results. This makes it easier to debug the scientific meaning of the map before optimizing the interface.

## Do not overcommit to one data provider

INSPIRE is likely the most natural first provider for high-energy physics, but papercone should remain provider-agnostic.

## Map first, intelligence later

The first milestone is not to infer research taste perfectly. The first milestone is to make a useful local research map visible.
