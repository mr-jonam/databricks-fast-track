---
title: Lab 03 - Production Design Review
aliases: [Databricks Architecture Lab]
tags: [databricks, lab, architecture, operations, intermediate]
difficulty: intermediate
estimated_time: 45 minutes
updated: 2026-09-22
---

# Lab 03: Production Design Review

## Scenario

Hourly customer events arrive as JSON files. Analysts need a dashboard by 15 minutes past the hour. Source files can arrive 24 hours late and schemas add optional fields. Personal fields must be restricted. A daily correction file changes past records.

## Design

Write a one-page proposal covering:

- ingestion mode and file discovery
- Bronze, Silver, Gold contracts
- stable keys and correction ordering
- schema evolution and rescued data
- late-data policy and dashboard freshness
- Unity Catalog layout, owners, groups, and sensitive-field controls
- Job versus pipeline responsibilities
- compute and cost starting point
- SLOs, quality checks, alerts, and replay procedure
- CI/CD and rollback boundaries

## Review rubric

| Area | Strong answer |
|---|---|
| Correctness | Handles duplicates, corrections, and late files deterministically |
| Recoverability | Bronze/replay state retained; checkpoints and cleanup understood |
| Governance | Group grants, least privilege, classification, no raw bypass |
| Operations | Freshness, volume, quality, cost, and owner are observable |
| Simplicity | Uses managed capabilities where they satisfy requirements |

## Failure injection

Explain the behavior when:

1. the same file is delivered twice;
2. an update is older than the current entity;
3. Gold fails after Silver commits;
4. a new required field appears as null;
5. the dashboard refreshes while the hourly load is incomplete.

Use [[Decision Trees]], [[Streaming and Auto Loader]], and [[Unity Catalog Governance]] only after drafting your own answer.
