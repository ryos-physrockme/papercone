# Cycle 5: personal anchors

Goal: put the researcher's own position on the papercone map.

## Desired experience

The user can register papers, saved papers, notes, drafts, and search queries as pins on the map.

Examples:

- own CSDR paper
- saved TTbar paper
- draft idea about AI-assisted integrability search
- query about sigma-model deformations

## Initial model

An anchor is a pseudo-node that can eventually share the same embedding space as papers.

Fields:

- id
- kind
- title
- text
- tags
- linked paper ID

## Later behavior

- embed anchors with the same embedder as papers
- render anchor pins separately from paper nodes
- boost frontier and path scores near personal anchors
