# papercone

papercone is a personal research map for navigating citation cones, semantic neighborhoods, and emerging research frontiers.

The first milestone is intentionally small: represent a local citation cone, validate its graph structure, and export/import it as JSON for later visualization.

## Development

```bash
pip install -e '.[dev]'
pytest
ruff check .
```

## Write the demo graph

```bash
python -m papercone.cli write-demo --out examples/demo_graph.json
# or, after installation:
papercone write-demo --out examples/demo_graph.json
```

The demo graph is a tiny fixture with a seed paper, one reference, one later citation, and directed citation relations.
