# Cycle 2: provider integration

Goal: fetch a real seed paper and its one-hop citation cone from an external scholarly data source.

## Preferred first provider

INSPIRE is the likely first provider because the initial target workflows are high-energy physics and mathematical physics.

## Desired experience

A user enters an arXiv ID or provider record ID. papercone fetches:

- paper metadata
- references
- citations when available
- normalized identifiers

Then papercone exports a local graph snapshot.

## First implementation sketch

```text
papercone providers fetch arxiv:2305.01421 --provider inspire --depth 1 --out .data/csdr_cone.json
```

## Design constraints

- Keep provider-specific raw responses out of the core model.
- Cache responses locally to avoid unnecessary API calls.
- Keep a provider protocol so OpenAlex and Semantic Scholar can be added later.
- Prefer explicit normalized IDs over ambiguous titles.
