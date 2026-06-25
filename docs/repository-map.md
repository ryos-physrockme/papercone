# Repository map

```text
papercone/
  docs/
    product-vision.md
    roadmap.md
    architecture.md
    principles.md
    cycle-*.md
  examples/
    demo_graph.json
  src/papercone/
    anchors/
    core/
    embedding/
    layout/
    providers/
    scoring/
    search/
  tests/
  pyproject.toml
```

## Main package areas

- `core`: stable domain concepts such as papers, edges, graphs, coordinates, and exports.
- `providers`: adapters for external scholarly data sources.
- `embedding`: embedding and projection interfaces for semantic layout.
- `layout`: visual coordinate conventions, including publication time as z-axis.
- `anchors`: user-defined personal research map pins.
- `search`: query jump and nearest-neighbor navigation helpers.
- `scoring`: frontier and path scoring primitives.
