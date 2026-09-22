---
title: Lab 01 - Delta Table Lifecycle
aliases: [Delta Lab]
tags: [databricks, lab, delta-lake, beginner]
difficulty: beginner
estimated_time: 35 minutes
updated: 2026-09-22
---

# Lab 01: Delta Table Lifecycle

## Goal

Create, modify, merge, inspect, and safely clean up a Delta table.

## Setup

Use a disposable schema. Confirm every destructive statement before running it.

```sql
CREATE SCHEMA IF NOT EXISTS main.training;
USE CATALOG main;
USE SCHEMA training;

CREATE OR REPLACE TABLE orders (
  order_id BIGINT,
  status STRING,
  amount DECIMAL(12,2),
  source_updated_at TIMESTAMP
) USING DELTA;
```

## Exercise

1. Insert two orders.
2. Create a temporary source view containing one update and one new order.
3. `MERGE` on `order_id`, accepting a matched update only when its source timestamp is newer.
4. Inspect table history and previous versions.
5. Try a write with an incompatible type and explain the result.

Start from [01_delta_basics.sql](../examples/01_delta_basics.sql), but type the `MERGE` yourself.

## Assertions

```sql
SELECT COUNT(*) = 3 AS has_three_orders FROM orders;
SELECT COUNT(*) = COUNT(DISTINCT order_id) AS keys_are_unique FROM orders;
SELECT status = 'shipped' AS update_applied FROM orders WHERE order_id = 1;
```

## Reflection

- Which table version introduced the update?
- What would happen if the source had two rows for `order_id = 1`?
- Which retention policy protects your recovery requirement?

## Cleanup

```sql
DROP TABLE IF EXISTS main.training.orders;
```

Related: [[04 - Delta Lake Essentials]], [[Delta Lake Performance and Reliability]].
