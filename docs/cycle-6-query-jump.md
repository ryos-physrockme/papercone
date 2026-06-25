# Cycle 6: query jump

Goal: turn a free-form research idea into a location on the map.

## Desired experience

The user types a query such as:

```text
AI-assisted search for integrable deformations of nonlinear sigma models
```

papercone embeds the query, finds nearby papers and anchors, and moves the camera to that region.

## First implementation idea

- use the same embedding interface as papers and anchors
- compute nearest neighbors in the current local graph snapshot
- expose the result as both a list and a target coordinate

## Later behavior

- smooth camera transition
- query pins
- query history
- semantic path from a personal anchor to the query region
