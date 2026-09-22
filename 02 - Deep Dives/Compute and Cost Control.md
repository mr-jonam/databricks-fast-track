---
title: Compute and Cost Control
aliases: [Databricks Compute, FinOps for Databricks]
tags: [databricks, compute, cost, performance, deep-dive]
difficulty: intermediate
estimated_time: 35 minutes
updated: 2026-09-22
---

# Compute and Cost Control

## Start with workload shape

| Workload | Starting point | Reconsider when |
|---|---|---|
| Ad hoc notebook | Serverless interactive | Unsupported library/network/runtime requirement |
| Scheduled task | Serverless job compute | Specialized hardware or unsupported configuration |
| BI/dashboard | Serverless SQL warehouse | Region/feature or isolation constraints |
| Long-lived custom Spark | Classic standard/dedicated | Administration exceeds the value of customization |

Serverless removes infrastructure tuning but not query, data layout, concurrency, or budget responsibility.

## Cost equation

Think in four multipliers:

```text
cost ≈ runtime × compute rate × concurrency × frequency
```

Optimize the largest measured multiplier. A bigger machine that halves runtime may cost less—or more. Measure total workload cost and SLA, not only duration.

## High-value controls

- right-size SQL warehouses and use auto-stop
- prefer job compute to always-on interactive compute for automation
- tag/attribute usage to teams, products, and environments
- set policies and permissions around who can create specialized compute
- cap concurrency or rate where product controls support it
- alert on spend trends and abnormal unit cost, not only a monthly total
- remove accidental full scans and repeated recomputation

## Performance before scaling

Inspect:

1. data scanned versus data returned
2. filters and projection pushdown
3. shuffles, skew, spills, and long-tail tasks
4. join strategy and cardinality
5. small-file count and data layout
6. repeated queries and cache suitability

Only then decide whether more compute is the correct fix.

## Cost metrics that reveal waste

- cost per successful pipeline run
- cost per GB or million records processed
- idle versus active time
- retry cost
- warehouse queue time and concurrency
- cost by tag, team, product, and environment
- jobs that succeed with zero or unexpected input

## Official reference

- [Compute](https://docs.databricks.com/aws/en/compute/)

Related: [[02 - Workspace, Notebooks, and Compute]], [[Monitoring and System Tables]].
