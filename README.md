# Databricks Fast Track: the 80/20 Lakehouse Guide

Learn the Databricks Data Intelligence Platform quickly, then deepen the parts that matter to your role. This repository is an **English, Obsidian-ready learning vault** with concise explanations, runnable SQL and PySpark examples, labs, decision guides, tips, and production-minded practices.

> The 80/20 claim is a prioritization principle, not a measured product-coverage guarantee: focus first on the small set of concepts that unlock most day-to-day Databricks work.

## What you will learn

- The lakehouse mental model: workspace, compute, Spark, Delta Lake, and Unity Catalog
- SQL and PySpark transformations without unnecessary Spark theory
- Bronze → Silver → Gold data design and incremental ingestion
- Delta Lake transactions, `MERGE`, history, optimization, and change data
- Governance, lineage, permissions, and discoverability with Unity Catalog
- Automation with Lakeflow Jobs and Lakeflow pipelines
- Databricks SQL, AI/BI, MLflow, system tables, cost, security, and CI/CD
- Practical troubleshooting and production decision rules

## Start in 60 seconds

1. Clone or download the repository.
2. Open the repository folder as an [Obsidian](https://obsidian.md/) vault, or read it directly on GitHub.
3. Open [[00 - Start Here]].
4. Follow [[00 - The 80-20 Learning Path]] for one focused learning day.
5. Run examples in a Databricks workspace using a catalog and schema you control.

No Obsidian community plugin is required. Wikilinks, backlinks, tags, properties, and the graph work with core features.

## Learning map

| Track | Time | Outcome |
|---|---:|---|
| [[00 - The 80-20 Learning Path\|80/20 Fast Track]] | 5 hours | Navigate, query, transform, govern, and automate a small lakehouse workflow |
| [[08 - Capstone - From Files to Gold\|Capstone]] | 60–90 min | Build a complete Bronze → Silver → Gold scenario |
| [[00 - Deep Dives Index\|Deep Dives]] | Pick as needed | Production depth in engineering, analytics, governance, AI, and operations |
| [[00 - Reference Index\|Reference]] | On demand | Cheatsheets, decisions, glossary, and troubleshooting |

## Repository structure

```text
.
├── 00 - Start Here.md
├── 01 - Databricks 80-20/    # the focused first-day path
├── 02 - Deep Dives/          # complete topic-focused notes
├── 03 - Reference/           # cheatsheets, glossary, decision guides
├── 04 - Labs/                # guided hands-on practice
├── examples/                 # Databricks SQL and Python source notebooks
├── scripts/                  # vault validation
└── .obsidian/                # safe, shared vault settings
```

## Prerequisites

- A Databricks workspace; [Databricks Free Edition](https://www.databricks.com/learn/free-edition) is enough for many introductory exercises.
- Basic SQL helps. Python is optional for the first pass.
- Permission to create objects in a Unity Catalog catalog/schema, or adapt examples to your environment.

Examples use `main.training`. Replace it with a namespace you can write to. Cloud-specific setup is intentionally separated from platform concepts.

## Current terminology

This vault follows current product terminology as of September 2026:

- **Lakeflow Jobs** for workflow orchestration
- **Lakeflow pipelines**, built on Apache Spark Declarative Pipelines, for declarative batch and streaming pipelines
- **Declarative Automation Bundles**, formerly Databricks Asset Bundles, for project-as-code delivery

The notes include older names only where they improve searchability. Product interfaces evolve; verify preview status and cloud/region availability in the linked official documentation.

## Validate the vault

```powershell
py scripts/validate_vault.py
```

The validator checks required frontmatter, Databricks tags, and unresolved local wikilinks. GitHub Actions runs the same check on every change.

## Contributing

Small, focused improvements are welcome. Keep explanations skimmable, prefer an executable example over a long paragraph, link to official sources, and never commit credentials or real customer data. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License and independence

Educational content is licensed under [CC BY 4.0](LICENSE-DOCS.md). Code and configuration are licensed under [Apache-2.0](LICENSE). See [NOTICE](NOTICE) and [LICENSE-DECISION.md](LICENSE-DECISION.md) for scope and provenance.

This is an independent learning project and is not affiliated with or endorsed by Databricks, Inc. Databricks and related product names belong to their respective owners.

## Search keywords

Databricks tutorial, Databricks training, lakehouse, Delta Lake, Apache Spark, PySpark, Databricks SQL, Unity Catalog, Lakeflow Jobs, Lakeflow pipelines, Auto Loader, MLflow, data engineering, data analytics, medallion architecture, Obsidian learning vault.
