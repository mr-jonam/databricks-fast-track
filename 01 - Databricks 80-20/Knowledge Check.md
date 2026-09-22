---
title: Knowledge Check
aliases: [Databricks 80-20 Quiz]
tags: [databricks, quiz, learning-path, beginner]
difficulty: beginner
estimated_time: 15 minutes
updated: 2026-09-22
---

# Knowledge Check

Answer before opening the hints.

1. What persists when compute terminates?
2. Why can SQL and PySpark have similar performance?
3. What does Delta Lake add to Parquet?
4. Why should a `MERGE` source be deduplicated?
5. Which medallion layer preserves source truth?
6. Name the three levels in a standard Unity Catalog table name.
7. When do you choose a Job over a pipeline?
8. Why must a retried task be idempotent?
9. What is the first evidence to inspect for a slow SQL query?
10. Why is time travel not a backup policy?

## Hints and answers

1. Data and governed objects persist; ephemeral compute state does not.
2. Both are translated into Spark logical and physical plans.
3. A transaction log and table semantics: ACID commits, schema controls, history, and reliable changes.
4. Multiple source rows for one target key create ambiguous updates or failures.
5. Bronze.
6. Catalog, schema, object.
7. A Job coordinates heterogeneous tasks and control flow; a pipeline declares dataset flows and dependencies.
8. A retry can repeat side effects and create duplicate or inconsistent output.
9. Query profile/plan, scan volume, exchanges, skew, and input/output metrics.
10. Old data availability depends on retention and file cleanup, and it does not replace independent recovery controls.

## Score

- **9–10:** Start role-specific deep dives.
- **7–8:** Revisit the two weakest modules, then continue.
- **0–6:** Re-run the fast path with the capstone; do not memorize product menus.
