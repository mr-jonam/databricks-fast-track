---
title: Delta Lake Essentials
aliases: [Delta Essentials]
tags: [databricks, delta-lake, tables, beginner]
difficulty: beginner
estimated_time: 40 minutes
updated: 2026-09-22
---

# Delta Lake Essentials

## Why it matters

Delta Lake extends Parquet data files with a transaction log. On Databricks, Delta is the default table format and enables reliable concurrent writes, schema controls, table history, updates, deletes, and merges.

## The small command set with large reach

```sql
CREATE OR REPLACE TABLE main.training.orders (
  order_id BIGINT,
  customer_id BIGINT,
  order_ts TIMESTAMP,
  amount DECIMAL(12,2)
) USING DELTA;

INSERT INTO main.training.orders VALUES
  (1, 101, TIMESTAMP '2026-09-22 09:00:00', 42.50);

DESCRIBE DETAIL main.training.orders;
DESCRIBE HISTORY main.training.orders;
```

## Idempotent upsert with `MERGE`

```sql
MERGE INTO main.training.orders AS target
USING main.training.order_updates AS source
ON target.order_id = source.order_id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *;
```

`MERGE` is only as correct as its key. Deduplicate the source first; multiple source rows matching one target row can make results ambiguous or fail.

## History and time travel

```sql
SELECT * FROM main.training.orders VERSION AS OF 0;
DESCRIBE HISTORY main.training.orders;
```

Time travel is operational convenience, not a backup policy. Retention and `VACUUM` determine which old files remain available.

## Managed versus external tables

- **Managed:** Unity Catalog controls governance and underlying storage lifecycle. Prefer this by default.
- **External:** Unity Catalog governs the object, but another system or policy controls the storage lifecycle. Use when that separation is intentional.

Never edit Delta data files or `_delta_log` directly.

## Optimization rules

- Let platform defaults and predictive/automatic optimization do their job where available.
- Prefer liquid clustering for evolving access patterns when supported; do not copy old partitioning recipes blindly.
- Run `OPTIMIZE` or choose clustering based on evidence from scan size and query profiles.
- Use `VACUUM` carefully; aggressive retention can break readers or eliminate recovery history.

## Checkpoint

What gives Delta tables ACID behavior? The transaction log coordinates table versions and atomic commits over the underlying files.

Next: [[05 - Medallion ETL]]. For depth: [[Delta Lake Performance and Reliability]].
