---
title: Lakeflow Pipelines
aliases: [Spark Declarative Pipelines, Delta Live Tables, DLT]
tags: [databricks, lakeflow, pipelines, data-engineering, deep-dive]
difficulty: intermediate
estimated_time: 40 minutes
updated: 2026-09-22
---

# Lakeflow Pipelines

Lakeflow pipelines provide declarative batch and streaming data pipelines in SQL and Python. They build on Apache Spark Declarative Pipelines and add managed production capabilities such as expectations, AUTO CDC, and event logs.

## Dataset choices

- **Streaming table:** incrementally processes records from a streaming source.
- **Materialized view:** maintains a query result, incrementally when supported.
- **Temporary view:** pipeline-scoped intermediate logic.
- **Sink:** writes to an external target or supported destination.

## Current Python form

```python
from pyspark import pipelines as dp
from pyspark.sql import functions as F


@dp.table(name="bronze_orders")
def bronze_orders():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load("/Volumes/main/training/landing/orders")
    )


@dp.materialized_view(name="daily_revenue")
def daily_revenue():
    return (
        spark.read.table("bronze_orders")
        .where(F.col("amount") >= 0)
        .groupBy(F.to_date("order_ts").alias("order_date"))
        .agg(F.sum("amount").alias("revenue"))
    )
```

Dataset functions describe a graph. Avoid side effects inside them because the engine evaluates definitions to plan and run the pipeline.

## Expectations

Use data quality expectations to record, drop, or fail invalid records according to impact. Pair rules with a quarantine strategy where investigation and replay matter. A dropped-row count without retained context is often insufficient.

## AUTO CDC

AUTO CDC handles change data capture into streaming tables and supports common SCD Type 1 and Type 2 patterns. Define keys, sequencing, and deletion semantics explicitly. Validate duplicates, out-of-order changes, and tombstones with representative source data.

## When a pipeline fits

Use it when dataset dependencies, incremental processing, schema handling, and quality controls are central. Use a Lakeflow Job around it when the broader workflow includes non-pipeline tasks, cross-system control flow, or downstream publishing steps.

## Production checklist

- target catalog/schema and run identity are explicit
- source and target contracts are documented
- update mode and full-refresh consequences are understood
- quality failures are observable and actionable
- event log and freshness metrics are monitored
- development and production settings are separated in code/configuration

## Official references

- [What are Lakeflow pipelines?](https://docs.databricks.com/aws/en/ldp/concepts)
- [Python development](https://docs.databricks.com/aws/en/ldp/developer/python-dev)

Related: [[07 - Jobs, Pipelines, and Operations]], [[Lakeflow Jobs and Orchestration]].
