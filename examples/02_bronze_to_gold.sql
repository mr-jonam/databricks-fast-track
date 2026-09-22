-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Small Bronze → Silver → Gold example
-- MAGIC The inline values stand in for already-ingested Bronze records.

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS main.training;

CREATE OR REPLACE TABLE main.training.bronze_orders AS
SELECT * FROM VALUES
  ('1', '2026-09-22T09:00:00Z', '42.50',  '2026-09-22T09:01:00Z', 'orders-001.json'),
  ('2', '2026-09-22T09:05:00Z', '19.99',  '2026-09-22T09:06:00Z', 'orders-001.json'),
  ('2', '2026-09-22T09:05:00Z', '19.99',  '2026-09-22T09:07:00Z', 'orders-002.json'),
  (NULL, '2026-09-22T09:10:00Z', '-5.00', '2026-09-22T09:11:00Z', 'orders-002.json')
AS raw(order_id, order_ts, amount, ingestion_ts, source_file);

-- COMMAND ----------

CREATE OR REPLACE TABLE main.training.silver_orders AS
SELECT order_id, order_ts, amount, ingestion_ts, source_file
FROM (
  SELECT
    CAST(order_id AS BIGINT) AS order_id,
    CAST(order_ts AS TIMESTAMP) AS order_ts,
    CAST(amount AS DECIMAL(12,2)) AS amount,
    CAST(ingestion_ts AS TIMESTAMP) AS ingestion_ts,
    source_file,
    ROW_NUMBER() OVER (
      PARTITION BY order_id ORDER BY CAST(ingestion_ts AS TIMESTAMP) DESC
    ) AS rn
  FROM main.training.bronze_orders
  WHERE order_id IS NOT NULL AND CAST(amount AS DECIMAL(12,2)) >= 0
)
WHERE rn = 1;

CREATE OR REPLACE VIEW main.training.quarantine_orders AS
SELECT *
FROM main.training.bronze_orders
WHERE order_id IS NULL OR CAST(amount AS DECIMAL(12,2)) < 0;

-- COMMAND ----------

CREATE OR REPLACE TABLE main.training.gold_daily_revenue AS
SELECT
  CAST(order_ts AS DATE) AS order_date,
  COUNT(*) AS orders,
  SUM(amount) AS revenue
FROM main.training.silver_orders
GROUP BY CAST(order_ts AS DATE);

SELECT * FROM main.training.gold_daily_revenue ORDER BY order_date;
