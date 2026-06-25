# Cycle 3: static papercone view

Goal: make the first map visible.

## Desired experience

A browser view displays a small citation cone. Papers are points, citation relations are edges, and publication time is represented by the z-axis.

## Initial coordinate convention

- `x`: semantic projection dimension 1, or fixture x before embeddings exist
- `y`: semantic projection dimension 2, or fixture y before embeddings exist
- `z`: publication year or publication timestamp

## Minimum UI

- load `examples/demo_graph.json`
- render nodes and edges
- distinguish seed, references, and citations
- hover to see title and year

## Later UI ideas

- hand tool / camera navigation
- smooth jump to query location
- cluster slicing by x-y plane
- frontier highlights
- path overlay
