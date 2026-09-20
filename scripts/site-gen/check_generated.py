#!/usr/bin/env python3
"""Fail when checked-in generated pages are stale without modifying them."""

import contextlib
import difflib
import pathlib
import shutil
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
GENERATOR = ROOT / "scripts" / "site-gen" / "gen.py"
OUTPUT = ROOT / "src"
GENERATED_FILES = (
    "index.html",
    "gtm-leadership.html",
    "how-i-operate.html",
    "career.html",
    "human-data-operating-layer.html",
    "agent-company.html",
)


@contextlib.contextmanager
def temporary_output():
    with tempfile.TemporaryDirectory(prefix="patrick-severs-site-") as directory:
        destination = pathlib.Path(directory) / "src"
        shutil.copytree(OUTPUT, destination)
        yield destination


def render(destination):
    source = GENERATOR.read_text()
    source = source.replace('OUT = pathlib.Path(__file__).resolve().parents[2]/"src"', f'OUT = pathlib.Path({str(destination)!r})')
    exec(compile(source, str(GENERATOR), "exec"), {"__name__": "__main__", "__file__": str(GENERATOR)})


def main():
    with temporary_output() as generated:
        render(generated)
        stale = []
        for filename in GENERATED_FILES:
            expected = (generated / filename).read_text()
            actual = (OUTPUT / filename).read_text()
            if actual != expected:
                stale.append(filename)
                print(f"stale: {filename}")
                print("".join(difflib.unified_diff(
                    actual.splitlines(keepends=True),
                    expected.splitlines(keepends=True),
                    fromfile=f"src/{filename}",
                    tofile=f"generated/{filename}",
                    n=2,
                )))
        if stale:
            raise SystemExit(f"{len(stale)} generated file(s) are stale. Run: python3 scripts/site-gen/gen.py")
    print("Generated pages are current.")


if __name__ == "__main__":
    main()
