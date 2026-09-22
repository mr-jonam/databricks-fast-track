---
title: Monitoring and System Tables
aliases: [Databricks Observability, System Tables]
tags: [databricks, monitoring, system-tables, observability, deep-dive]
difficulty: intermediate
estimated_time: 40 minutes
updated: 2026-09-22
---

# Monitoring and System Tables

## Monitor outcomes, not only infrastructure

Use four signal groups:

| Group | Examples |
|---|---|
| Reliability | run success, retries, queue time, duration, last successful partition |
| Data | freshness, input/output rows, duplicates, nulls, expectation failures |
| Performance | bytes scanned, shuffle/spill, task skew, warehouse queueing |
| Cost/security | usage by tag, unit cost, grants, access events, anomalous queries |

A green job with stale or empty output is an incident.

## System tables

System tables expose account-level operational data through governed schemas. Common areas include billing/usage, audit, query history, compute, and Lakeflow job activity. Availability, retention, and schema vary by cloud/region and release.

Example pattern—adapt field names from the current reference:

```sql
SELECT
  date_trunc('day', usage_start_time) AS usage_day,
  sku_name,
  SUM(usage_quantity) AS usage
FROM system.billing.usage
WHERE usage_start_time >= current_timestamp() - INTERVAL 30 DAYS
GROUP BY 1, 2
ORDER BY 1 DESC, 3 DESC;
```

Do not make finance claims from raw usage quantity without joining the correct price/reference data and considering corrections.

## SLO examples

- Freshness: Gold table updated by 07:00 in the agreed timezone.
- Completeness: Daily input volume is within a learned or contractual range.
- Quality: Invalid rows stay below threshold, with zero critical-key violations.
- Reliability: 99% of scheduled runs finish before the business deadline.
- Efficiency: Unit cost stays within an agreed envelope.

## Alert design

Every alert needs:

- a condition with a stable threshold or anomaly rule
- severity and user/business impact
- owner and escalation channel
- relevant run/table/query identifiers
- a runbook with first evidence to inspect
- suppression/deduplication to prevent alert storms

## Dashboard layers

1. Executive/service health: SLOs and current impact.
2. Operator view: failures, freshness, volume, cost anomalies.
3. Diagnostic detail: task/query IDs, plans, logs, input versions.

## Official references

- [System tables](https://docs.databricks.com/aws/en/admin/system-tables/)
- [Lakeflow Jobs system tables](https://docs.databricks.com/aws/en/admin/system-tables/jobs)

Related: [[Troubleshooting Playbook]], [[Compute and Cost Control]].
