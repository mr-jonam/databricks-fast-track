-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Delta Lake basics
-- MAGIC Run only in a disposable schema you are allowed to modify.

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS main.training;
USE CATALOG main;
USE SCHEMA training;

CREATE OR REPLACE TABLE orders (
  order_id BIGINT,
  status STRING,
  amount DECIMAL(12,2),
  source_updated_at TIMESTAMP
) USING DELTA;

INSERT INTO orders VALUES
  (1, 'placed', 42.50, TIMESTAMP '2026-09-22 09:00:00'),
  (2, 'placed', 19.99, TIMESTAMP '2026-09-22 09:05:00');

-- COMMAND ----------

CREATE OR REPLACE TEMP VIEW order_updates AS
SELECT * FROM VALUES
  (1, 'shipped', 42.50, TIMESTAMP '2026-09-22 10:00:00'),
  (3, 'placed', 75.00, TIMESTAMP '2026-09-22 10:05:00')
AS updates(order_id, status, amount, source_updated_at);

MERGE INTO orders AS target
USING order_updates AS source
ON target.order_id = source.order_id
WHEN MATCHED AND source.source_updated_at >= target.source_updated_at THEN
  UPDATE SET *
WHEN NOT MATCHED THEN
  INSERT *;

-- COMMAND ----------

SELECT * FROM orders ORDER BY order_id;
DESCRIBE HISTORY orders;
DESCRIBE DETAIL orders;
