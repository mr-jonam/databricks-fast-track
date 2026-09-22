---
title: Tips and Tricks
aliases: [Databricks Tips]
tags: [databricks, tips, productivity, reference]
difficulty: beginner
estimated_time: 15 minutes
updated: 2026-09-22
---

# Tips and Tricks

## Everyday productivity

- Set catalog and schema explicitly at the start of interactive work.
- Fully qualify production objects even when a default exists.
- Use `LIMIT` for preview, but validate with counts and invariants.
- Keep one “expected grain” sentence beside every durable table.
- Add table and column comments while context is fresh.
- Use temporary views to make multi-step SQL readable; use durable views only for a real contract.
- Pin critical dashboard filters and show their active values.

## SQL and Spark

- Replace `SELECT *` in production with a deliberate column list.
- Use `EXPLAIN` or query profile before guessing about performance.
- Check join-key uniqueness before and after joins.
- Prefer built-in functions over UDFs.
- Repartition only for a measured reason; each repartition can cause a shuffle.
- Do not cache a DataFrame used once.
- Avoid converting distributed data to pandas unless its bounded size is proven.

## Delta

- Use `DESCRIBE HISTORY` during incident analysis.
- Deduplicate a `MERGE` source deterministically.
- Add source timestamps and ingestion timestamps; they answer different questions.
- Treat `VACUUM` retention as a recovery/compliance decision.
- Prefer stable business keys over generated row positions.

## Jobs and operations

- Put business date/timezone in parameters rather than relying on “today.”
- Add timeouts so hung work becomes visible.
- Alert after meaningful failure, not every automatic retry.
- Track the last successfully published business partition.
- Make cleanup a separate, narrowly scoped, auditable task.
- For backfills, bound dates and concurrency explicitly.

## Cost

- Auto-stop interactive and SQL compute.
- Attribute usage with consistent tags/policies.
- Look for retry loops and empty successful runs.
- Compare cost per output unit, not only total DBUs.
- Reduce scanned data before buying more compute.

## Obsidian

- Use `Ctrl/Cmd+O` to jump between notes.
- Open backlinks to follow prerequisites and related concepts.
- Filter graph/tag views by `#databricks`, `#deep-dive`, or your role.
- Add personal notes in a separate folder so upstream updates remain easy to merge.

Related: [[00 - Reference Index]], [[Troubleshooting Playbook]].
