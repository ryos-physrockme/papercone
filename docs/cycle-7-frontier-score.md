# Cycle 7: frontier scoring

Goal: highlight regions that may correspond to emerging frontiers, bridges, or underexplored gaps.

## Desired experience

The map should not merely show many papers. It should help the user notice promising directions.

## Initial score sketch

```text
frontier_score =
  recency_score
+ citation_velocity_score
+ cluster_growth_score
+ bridge_score
+ semantic_novelty_score
+ personal_relevance_score
- saturation_penalty
```

## Interpretation

- recency: newer papers receive a boost
- citation velocity: recently growing papers receive a boost
- cluster growth: regions with increasing density receive a boost
- bridge score: papers connecting clusters receive a boost
- semantic novelty: papers slightly outside dense clusters receive a boost
- personal relevance: papers reachable from user anchors receive a boost
- saturation penalty: old, very dense, already mature regions are deprioritized

## Caution

This score is a heuristic. It should be presented as a navigation aid, not an objective measure of research value.
