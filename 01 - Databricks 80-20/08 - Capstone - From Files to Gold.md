---
title: Capstone - From Files to Gold
aliases: [80-20 Capstone, Files to Gold]
tags: [databricks, capstone, lab, medallion, beginner]
difficulty: beginner
estimated_time: 75 minutes
updated: 2026-09-22
---

# Capstone: From Files to Gold

## Scenario

Build a small order pipeline. Raw JSON arrives in governed storage. Bronze preserves it, Silver validates and deduplicates orders, and Gold publishes daily revenue.

## Success criteria

- Re-running the workflow creates no duplicates.
- Invalid rows are visible rather than silently lost.
- Gold is derived only from validated Silver data.
- Objects use three-level Unity Catalog names.
- A future operator can identify freshness, row counts, and failures.

## Steps

1. Create a disposable `main.training` schema or equivalent.
2. Run [[Lab 01 - Delta Table Lifecycle]] to practice safe table changes.
3. Use [01_delta_basics.sql](../examples/01_delta_basics.sql) as a syntax reference.
4. Create `bronze_orders` with source metadata.
5. Build `silver_orders` with typed fields and one record per `order_id`.
6. Route missing IDs or negative amounts to a quarantine view/table.
7. Build `gold_daily_revenue` with order count and total amount by date.
8. Add a late correction and use `MERGE` to update Silver.
9. Inspect `DESCRIBE HISTORY` for all changed tables.
10. Sketch the Lakeflow Job tasks, retry boundaries, and notification policy.

## Acceptance queries

```sql
-- No duplicate business keys
SELECT order_id, COUNT(*) AS n
FROM main.training.silver_orders
GROUP BY order_id
HAVING COUNT(*) > 1;

-- Gold reconciles with Silver
SELECT
  (SELECT SUM(amount) FROM main.training.silver_orders) AS silver_total,
  (SELECT SUM(revenue) FROM main.training.gold_daily_revenue) AS gold_total;

-- Inspect lineage and history
DESCRIBE HISTORY main.training.silver_orders;
```

Expected: the duplicate query returns zero rows and totals agree for the same business scope.

## Design review

Write one sentence for each:

- How is a replay detected?
- What is the stable key?
- Where are invalid rows counted?
- What happens if Gold fails after Silver succeeds?
- Who owns each production object?
- Which metric detects a “successful” run that processed zero unexpected rows?

## Cleanup

Only in your disposable schema:

```sql
DROP SCHEMA main.training CASCADE;
```

Do not run broad cleanup in a shared environment.

Finish with [[Knowledge Check]], then choose a [[00 - Deep Dives Index|deep dive]].
