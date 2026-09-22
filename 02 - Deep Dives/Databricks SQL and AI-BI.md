---
title: Databricks SQL and AI-BI
aliases: [Databricks SQL, AI-BI]
tags: [databricks, sql, ai-bi, analytics, deep-dive]
difficulty: intermediate
estimated_time: 35 minutes
updated: 2026-09-22
---

# Databricks SQL and AI/BI

Databricks SQL provides warehouse compute, SQL authoring, dashboards, alerts, semantic metric views, and ETL capabilities directly over governed lakehouse data.

## Warehouse choices

Start with serverless SQL warehouses where available. Size for workload latency and concurrency, then configure sensible auto-stop. Separate workloads only when isolation, ownership, or predictable performance requires it.

## Query workflow

1. Confirm the correct catalog/schema and data freshness.
2. Write the simplest correct query.
3. Inspect result cardinality and reconciliation totals.
4. Open query profile for slow/expensive queries.
5. Fix scans, joins, filters, and layout before scaling.

## Semantic consistency

Metric views or a governed semantic layer reduce the number of competing definitions for revenue, active customer, conversion, and other business metrics. Define grain, filters, time behavior, ownership, and certification. A shared formula without a shared definition is still inconsistent.

## Dashboard design

- one question per visual
- explicit units, time zones, refresh/freshness, and filters
- limited high-signal KPIs before detail
- drill paths that preserve context
- permissions inherited from governed sources
- performance tested with realistic concurrency and date ranges

## Query anti-patterns

- `SELECT *` in durable dashboards
- implicit cross joins or many-to-many joins
- transforming timestamps without an explicit timezone policy
- filtering a partition/clustering key through a function unnecessarily
- duplicating business logic in every dashboard
- trusting a successful refresh without freshness and row-volume checks

## Alerts

Alerts should indicate an actionable condition: failed freshness SLA, quality threshold, cost anomaly, or business event. Include owner, severity, observed value, threshold, and a runbook link.

## Official reference

- [Data warehousing on Databricks](https://docs.databricks.com/aws/en/sql)

Related: [[SQL Cheatsheet]], [[Monitoring and System Tables]].
