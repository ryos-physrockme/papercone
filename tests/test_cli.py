import json

from papercone.cli import main


def test_cli_write_demo(tmp_path) -> None:
    out = tmp_path / "demo.json"

    exit_code = main(["write-demo", "--out", str(out)])

    payload = json.loads(out.read_text(encoding="utf-8"))
    assert exit_code == 0
    assert len(payload["papers"]) == 3
