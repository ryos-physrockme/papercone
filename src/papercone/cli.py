"""Small command-line entry points for papercone."""

from __future__ import annotations

import argparse
from pathlib import Path

from papercone.core.fixtures import make_demo_graph
from papercone.core.jsonio import write_graph_json


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="papercone")
    subparsers = parser.add_subparsers(dest="command", required=True)

    demo = subparsers.add_parser("write-demo", help="Write the demo graph JSON.")
    demo.add_argument("--out", type=Path, default=Path("examples/demo_graph.json"))

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "write-demo":
        write_graph_json(make_demo_graph(), args.out)
        return 0

    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
