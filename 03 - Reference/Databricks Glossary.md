---
title: Databricks Glossary
aliases: [Glossary]
tags: [databricks, glossary, reference]
difficulty: beginner
estimated_time: 20 minutes
updated: 2026-09-22
---

# Databricks Glossary

**ACID** — Atomicity, consistency, isolation, and durability guarantees for transactions.

**Auto Loader** — Incremental file ingestion through the `cloudFiles` Structured Streaming source.

**Bronze / Silver / Gold** — Raw-preserving, validated/reusable, and business-serving layers in medallion architecture.

**Catalog / Schema / Object** — Three-level Unity Catalog namespace, commonly `catalog.schema.table`.

**Change Data Feed (CDF)** — Delta capability exposing row-level changes between table versions.

**Checkpoint** — Durable progress and state for a streaming query; logically belongs to one query.

**Compute** — Resources that execute workloads; distinct from persistent storage.

**DataFrame** — Distributed table-like abstraction transformed through Spark APIs.

**Declarative Automation Bundles** — Databricks project/resource delivery as code; formerly Asset Bundles.

**Delta Lake** — Open table storage layer adding a transaction log and reliable table operations over files.

**Driver / executor** — Spark coordination process and distributed worker processes.

**Idempotent** — Safe to repeat without changing the intended final result.

**Lakeflow Jobs** — Workflow orchestration for tasks, triggers, dependencies, parameters, and monitoring.

**Lakeflow pipelines** — Declarative batch/streaming data pipelines built on Spark Declarative Pipelines.

**Liquid clustering** — Delta data-layout approach using clustering keys without rigid directory partitions.

**Managed table** — Table whose governance and storage lifecycle are managed by Unity Catalog.

**Materialized view** — Stored query result maintained by the platform, incrementally where supported.

**Medallion architecture** — Layered pattern that increases quality and business meaning from Bronze to Gold.

**MLflow** — Open platform for ML/AI tracking, evaluation, registry, observability, and deployment workflows.

**Photon** — Databricks vectorized query engine used to accelerate supported SQL/DataFrame workloads.

**Shuffle** — Network redistribution of data, commonly caused by joins and aggregations.

**SQL warehouse** — Compute optimized for Databricks SQL workloads.

**Streaming table** — Delta table maintained with streaming/incremental semantics in Lakeflow pipelines.

**Unity Catalog** — Unified governance for data and AI assets, permissions, lineage, discovery, auditing, and sharing.

**Volume** — Unity Catalog governed storage for non-tabular files.

Related: [[01 - The Databricks Mental Model]], [[Official Resources]].
