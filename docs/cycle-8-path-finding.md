# Cycle 8: path finding

Goal: suggest a plausible path from a personal anchor to a frontier paper or cluster.

## Desired experience

The user selects an anchor and a target region. papercone returns a sequence of papers and concepts that forms a readable route.

Example shape:

```text
own CSDR paper
-> coset-space model building
-> sigma-model geometry
-> integrability and Lax pairs
-> AI-assisted integrability search
```

## Initial cost sketch

```text
cost(u, v) =
  semantic_distance
+ time_penalty
- citation_edge_bonus
- shared_topic_bonus
- personal_relevance_bonus
```

## Path output

A path should include:

- ordered papers or anchors
- why each step was chosen
- citation or semantic relation type
- reading priority
- optional missing background nodes

## Caution

A generated path is not a proof that the target is a good topic. It is a navigation hypothesis to inspect.
