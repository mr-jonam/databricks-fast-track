---
title: Streaming and Auto Loader
aliases: [Auto Loader Deep Dive, Structured Streaming]
tags: [databricks, streaming, auto-loader, data-engineering, deep-dive]
difficulty: intermediate
estimated_time: 40 minutes
updated: 2026-09-22
---

# Streaming and Auto Loader

## The practical model

Structured Streaming repeatedly executes an incremental query while maintaining progress and, for stateful operations, state. Auto Loader exposes the `cloudFiles` source to discover and ingest new files at scale.

“Streaming” describes processing semantics, not necessarily sub-second latency. A triggered incremental workload can be the simplest correct solution.

## Auto Loader baseline

```python
raw = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.schemaLocation", "/Volumes/main/training/checkpoints/orders_schema")
    .load("/Volumes/main/training/landing/orders")
)

query = (
    raw.writeStream
    .option("checkpointLocation", "/Volumes/main/training/checkpoints/orders_bronze")
    .trigger(availableNow=True)
    .toTable("main.training.bronze_orders")
)
```

Use unique durable locations. A checkpoint belongs to one logical query; reusing or deleting it changes processing guarantees.

## Core decisions

| Decision | Choose based on |
|---|---|
| Continuous vs triggered | Required latency, cost, source behavior, operational tolerance |
| Directory listing vs file events | Scale, cloud setup, cost, and supported features |
| Schema inference vs explicit schema | Contract stability and failure tolerance |
| Additive evolution vs rescue | Consumer compatibility and governance |
| Drop/stop/quarantine bad records | Business risk and recoverability |

Auto Loader discovery order is not an event-time guarantee. Design for late and out-of-order data.

## Stateful operations and watermarks

Aggregations, deduplication, and stream-stream joins may keep state. A watermark tells the engine how late data may arrive before state can be retired. It is a business correctness decision:

- Too short: valid late data can be excluded from stateful results.
- Too long: state grows, increasing cost and failure recovery time.

Measure real lateness distributions before choosing.

## Exactly-once: say what you mean

Auto Loader plus Delta and a stable checkpoint can provide exactly-once processing of discovered files into the sink. End-to-end side effects outside Delta—API calls, emails, or custom `foreachBatch` logic—need their own idempotency design.

## Operations checklist

- input rows/rate and processed rows/rate
- batch duration and backlog
- state size and late-record behavior
- checkpoint/storage health
- schema changes and rescued fields
- output freshness and duplicates
- restart behavior after code changes

## Official references

- [What is Auto Loader?](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader)
- [Structured Streaming on Databricks](https://docs.databricks.com/aws/en/structured-streaming/)

Related: [[05 - Medallion ETL]], [[Lakeflow Pipelines]].
