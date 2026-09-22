#!/usr/bin/env python3
"""Validate frontmatter and Obsidian wikilinks using only the standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {"README.md", "CONTRIBUTING.md", "LICENSE-DOCS.md", "LICENSE-DECISION.md"}
REQUIRED_KEYS = {"title", "tags", "difficulty", "estimated_time", "updated"}
WIKILINK = re.compile(r"!?(?:\[\[)([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def learning_notes() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if path.name not in EXCLUDED
        and ".github" not in path.parts
        and not path.name.startswith("LICENSE")
        and path.name not in {"AGENTS.md"}
    )


def note_names(paths: list[Path]) -> set[str]:
    names = {path.stem.casefold() for path in paths}
    names.update(path.relative_to(ROOT).with_suffix("").as_posix().casefold() for path in paths)
    return names


def validate() -> list[str]:
    errors: list[str] = []
    notes = learning_notes()
    known = note_names(notes)

    for path in notes:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        if not text.startswith("---\n"):
            errors.append(f"{relative}: missing YAML frontmatter")
            continue

        end = text.find("\n---\n", 4)
        if end == -1:
            errors.append(f"{relative}: unclosed YAML frontmatter")
            continue

        frontmatter = text[4:end]
        keys = {
            line.split(":", 1)[0].strip()
            for line in frontmatter.splitlines()
            if ":" in line
        }
        missing = REQUIRED_KEYS - keys
        if missing:
            errors.append(f"{relative}: missing frontmatter keys {sorted(missing)}")
        if not re.search(r"^tags:.*databricks", frontmatter, re.MULTILINE | re.IGNORECASE):
            errors.append(f"{relative}: tags must include databricks")

        for target in WIKILINK.findall(text):
            normalized = target.strip().replace("\\", "/").casefold()
            if normalized not in known and Path(normalized).name not in known:
                errors.append(f"{relative}: unresolved wikilink [[{target}]]")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Vault validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Vault validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
