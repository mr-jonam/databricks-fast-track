---
title: The 80-20 Learning Path
aliases: [Databricks 80-20, Fast Track]
tags: [databricks, learning-path, beginner]
difficulty: beginner
estimated_time: 5 hours
updated: 2026-09-22
---

# The 80/20 Learning Path

## The outcome

In one focused day, you should be able to explain the platform, explore governed data, transform it with SQL or PySpark, create reliable Delta tables, organize a medallion flow, and automate a small workload.

This is operational fluency, not mastery. It deliberately postpones cloud networking, unusual Spark tuning, advanced streaming state, enterprise identity design, and specialized AI features.

## Five-hour schedule

| Time | Module | Deliverable |
|---:|---|---|
| 25 min | [[01 - The Databricks Mental Model]] | Draw the platform from memory |
| 25 min | [[02 - Workspace, Notebooks, and Compute]] | Run SQL and Python on appropriate compute |
| 45 min | [[03 - Spark, DataFrames, and SQL]] | Transform the same dataset in SQL and PySpark |
| 40 min | [[04 - Delta Lake Essentials]] | Create, update, merge, and inspect a Delta table |
| 40 min | [[05 - Medallion ETL]] | Classify Bronze, Silver, and Gold responsibilities |
| 30 min | [[06 - Unity Catalog Essentials]] | Navigate and grant access through the namespace |
| 30 min | [[07 - Jobs, Pipelines, and Operations]] | Choose and sketch an automated workflow |
| 60–90 min | [[08 - Capstone - From Files to Gold]] | Build an end-to-end mini lakehouse |
| 15 min | [[Knowledge Check]] | Identify weak areas for a deep dive |

## The ten concepts that unlock most work

1. **Workspace is the collaboration surface; compute is what executes.**
2. **Spark DataFrames and SQL are two interfaces to the same distributed engine.**
3. **Tables are preferred interfaces; raw paths are implementation details.**
4. **Delta Lake adds transactions, schema controls, history, and efficient changes.**
5. **Unity Catalog uses `catalog.schema.object` and governs access plus lineage.**
6. **Bronze preserves; Silver validates; Gold serves a business purpose.**
7. **Incremental and idempotent processing beats repeated full reloads.**
8. **Lakeflow Jobs orchestrate tasks; Lakeflow pipelines declare data flows.**
9. **Serverless is the default starting point when supported; specialize compute for a reason.**
10. **Observe cost, quality, freshness, and failures—not only task success.**

## The 80/20 production rules

- Use SQL when the work is relational and your team reads SQL well.
- Use PySpark when you need programmatic composition, libraries, or complex logic.
- Prefer managed tables unless external lifecycle control is a real requirement.
- Re-run safely: design writes to be idempotent and use stable business keys.
- Filter early, select only needed columns, and inspect the query profile before tuning.
- Give permissions to groups, not individuals; give production ownership to groups.
- Treat notebooks as excellent exploration tools, not an excuse to skip source control.
- Start simple and measure. Partitioning, caching, and manual cluster tuning are not default answers.

## Exit test

Without notes, answer:

- What is the difference between Spark, Delta Lake, and Databricks?
- Why is `catalog.schema.table` important?
- When would you use a Job instead of a pipeline?
- What makes a pipeline safe to re-run?
- Where would you look first for a slow or expensive query?

If any answer is fuzzy, revisit that module. Otherwise continue with role-specific [[00 - Deep Dives Index|deep dives]].
