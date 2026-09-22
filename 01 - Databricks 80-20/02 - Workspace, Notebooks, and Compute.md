---
title: Workspace, Notebooks, and Compute
aliases: [Databricks Workspace Basics, Compute Basics]
tags: [databricks, notebooks, compute, beginner]
difficulty: beginner
estimated_time: 25 minutes
updated: 2026-09-22
---

# Workspace, Notebooks, and Compute

## The three surfaces you need first

- **Workspace:** files, Git folders, notebooks, and collaboration.
- **Catalog:** governed tables, volumes, models, functions, lineage, and permissions.
- **Jobs & Pipelines / SQL:** automation and consumption surfaces.

Names and navigation can vary by cloud and release. Learn the objects, not pixel positions.

## Notebook essentials

A notebook mixes Markdown with SQL, Python, Scala, or R cells. A language magic changes one cell:

```python
# Python cell
display(spark.table("samples.nyctaxi.trips").limit(10))
```

```sql
-- SQL cell, or use %sql in a Python-default notebook
SELECT * FROM samples.nyctaxi.trips LIMIT 10;
```

Use notebooks to explore, explain, and debug. For reusable production logic, prefer source files, tested functions, and versioned project deployment.

## Compute decision table

| Need | Start with | Why |
|---|---|---|
| Interactive notebook | Serverless interactive compute | Low administration and fast start where available |
| Automated job | Serverless job compute | Isolation and automatic lifecycle |
| SQL queries or dashboards | Serverless SQL warehouse | SQL-optimized and elastic |
| Custom runtime/network/library controls | Classic compute | More configuration, more responsibility |
| Single user or incompatible workload | Dedicated compute | Isolation for the assigned user/group |
| Shared compatible workloads | Standard compute | Cost-effective multi-user execution |

Serverless availability and limitations vary. Verify requirements before standardizing.

## Practical habits

- Stop idle classic compute; configure auto-termination.
- Do not install ad hoc libraries repeatedly if a managed environment or project dependency file fits.
- Keep secrets in approved secret/governance mechanisms, never in notebook cells.
- Pass job parameters explicitly; avoid hidden widget or session state.
- Clear notebook outputs that contain sensitive data before committing.

## Checkpoint

For an analyst running dashboards, choose a SQL warehouse—not an all-purpose interactive cluster. For a nightly isolated workflow, choose job/serverless compute when supported.

Next: [[03 - Spark, DataFrames, and SQL]]. For depth: [[Compute and Cost Control]].
