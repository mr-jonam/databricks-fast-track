# Project agent guide

## Purpose

English, Obsidian-ready training vault for learning Databricks quickly and then going deeper.

## Stack and build

- Markdown knowledge base with YAML frontmatter and Obsidian wikilinks.
- Runnable Databricks examples in SQL and Python under `examples/`.
- No build step. Validation uses Python standard library only.

## Entrypoints

- Reader entrypoint: `README.md`, then `00 - Start Here.md`.
- Fast path: `01 - Databricks 80-20/00 - The 80-20 Learning Path.md`.
- Advanced map: `02 - Deep Dives/00 - Deep Dives Index.md`.

## Tests and CI

- Local: `py scripts/validate_vault.py`
- CI: `.github/workflows/validate.yml`

## Configuration

- Obsidian preferences: `.obsidian/`.
- Funding metadata: `.github/FUNDING.yml`.

## Conventions

- Keep notes short, task-oriented, and linked in both directions where useful.
- Every learning note starts with YAML frontmatter and at least one `databricks` tag.
- Prefer current names: Lakeflow Jobs, Lakeflow pipelines, and Declarative Automation Bundles.
- Mention legacy names only to help readers search older material.
- Examples use `main.training` as the placeholder Unity Catalog namespace.
- Never add credentials, workspace URLs, account IDs, or private datasets.
- Content is CC BY 4.0; code samples are Apache-2.0. See `NOTICE`.
