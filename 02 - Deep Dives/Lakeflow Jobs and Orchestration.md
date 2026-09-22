---
title: Lakeflow Jobs and Orchestration
aliases: [Databricks Jobs Deep Dive, Workflows]
tags: [databricks, lakeflow, jobs, orchestration, deep-dive]
difficulty: intermediate
estimated_time: 35 minutes
updated: 2026-09-22
---

# Lakeflow Jobs and Orchestration

## Resource model

- **Job:** workflow definition, permissions, parameters, triggers, notifications.
- **Task:** unit of execution such as notebook, Python, SQL, dbt, pipeline, model, or condition.
- **Run:** one execution with resolved parameters and task states.
- **Trigger:** schedule, file/event arrival, or API/manual invocation where supported.

## DAG design rules

- Model real dependencies, not visual ordering.
- Keep business transformations in testable code, not in task plumbing.
- Pass identifiers or governed table names rather than large payloads between tasks.
- Prefer one clear responsibility per task and meaningful task keys.
- Fan out independent work; fan in only when an actual dependency exists.

## Parameters

Validate parameters at the boundary. Record effective values. Avoid environment-specific names buried in code; resolve them from deployment targets or configuration.

```text
business_date=2026-09-22
source_catalog=raw_prod
target_catalog=analytics_prod
run_mode=incremental
```

## Retries and repair runs

Retries are safe only when the task is idempotent. A repair run reruns failed/skipped work in an existing run context; understand whether upstream output is immutable or may have changed.

Classify failures:

- transient infrastructure/network → bounded retry with backoff
- capacity/rate limit → retry plus concurrency review
- bad data/contract → quarantine or fail, then remediate
- deterministic code defect → fix and redeploy; retries waste cost
- external side effect uncertainty → reconcile before retry

## Triggers

A schedule is simple but may run without data. File-arrival triggers can reduce latency and wasted runs but require clear completeness semantics. Continuous jobs fit always-on processing but increase operational responsibility.

## Observability

Monitor duration, queue time, retries, output freshness, processed volume, quality failures, compute cost, and the last successful business partition. “Run succeeded” is necessary, not sufficient.

## Official reference

- [Lakeflow Jobs](https://docs.databricks.com/aws/en/jobs)

Related: [[Monitoring and System Tables]], [[Declarative Automation Bundles and CI-CD]].
