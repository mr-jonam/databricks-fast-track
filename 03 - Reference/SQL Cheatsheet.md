---
title: SQL Cheatsheet
aliases: [Databricks SQL Cheatsheet]
tags: [databricks, sql, delta-lake, reference]
difficulty: beginner
estimated_time: 15 minutes
updated: 2026-09-22
---

# SQL Cheatsheet

Replace `main.training` with a namespace you control.

## Context and discovery

```sql
USE CATALOG main;
USE SCHEMA training;
SHOW TABLES;
DESCRIBE EXTENDED orders;
DESCRIBE DETAIL orders;
DESCRIBE HISTORY orders;
```

## Create and transform

```sql
CREATE OR REPLACE TABLE silver_orders
USING DELTA AS
SELECT
  CAST(order_id AS BIGINT) AS order_id,
  CAST(order_ts AS TIMESTAMP) AS order_ts,
  CAST(amount AS DECIMAL(12,2)) AS amount
FROM bronze_orders
WHERE order_id IS NOT NULL AND amount >= 0;
```

## Deduplicate deterministically

```sql
SELECT * EXCEPT (rn)
FROM (
  SELECT *, ROW_NUMBER() OVER (
    PARTITION BY order_id ORDER BY source_updated_at DESC, ingestion_ts DESC
  ) AS rn
  FROM bronze_orders
)
WHERE rn = 1;
```

## Upsert

```sql
MERGE INTO silver_orders AS t
USING deduplicated_updates AS s
ON t.order_id = s.order_id
WHEN MATCHED AND s.source_updated_at >= t.source_updated_at THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *;
```

## Quality checks

```sql
SELECT
  COUNT(*) AS rows,
  COUNT_IF(order_id IS NULL) AS missing_ids,
  COUNT_IF(amount < 0) AS negative_amounts,
  COUNT(DISTINCT order_id) AS distinct_orders
FROM silver_orders;
```

## Time and history

```sql
SELECT current_timestamp(), current_date();
SELECT * FROM orders VERSION AS OF 3;
SELECT * FROM orders TIMESTAMP AS OF '2026-09-22T09:00:00Z';
```

## Explain

```sql
EXPLAIN FORMATTED
SELECT customer_id, SUM(amount)
FROM silver_orders
GROUP BY customer_id;
```

## Permissions

```sql
GRANT USE CATALOG ON CATALOG main TO `training_readers`;
GRANT USE SCHEMA ON SCHEMA main.training TO `training_readers`;
GRANT SELECT ON TABLE main.training.silver_orders TO `training_readers`;
SHOW GRANTS ON TABLE main.training.silver_orders;
```

Related: [[04 - Delta Lake Essentials]], [[Databricks SQL and AI-BI]].
