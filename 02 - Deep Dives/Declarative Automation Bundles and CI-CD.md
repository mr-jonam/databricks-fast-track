---
title: Declarative Automation Bundles and CI-CD
aliases: [Databricks Asset Bundles, DABs, Databricks CI-CD]
tags: [databricks, bundles, devops, ci-cd, deep-dive]
difficulty: intermediate
estimated_time: 40 minutes
updated: 2026-09-22
---

# Declarative Automation Bundles and CI/CD

Declarative Automation Bundles—formerly Databricks Asset Bundles—package source, resource definitions, and environment targets so jobs, pipelines, dashboards, models, and related resources can be reviewed and deployed as code.

## Minimal lifecycle

```text
edit → unit test → bundle validate → plan/review → deploy to dev → integration test
     → approval → deploy to prod → observe → rollback/fix forward
```

## Conceptual structure

```text
databricks.yml
resources/
  job.yml
  pipeline.yml
src/
tests/
```

Keep business code in `src/`; keep resource wiring in configuration. Use target-specific variables and identity settings instead of copying entire projects per environment.

## Commands

```bash
databricks bundle validate -t dev
databricks bundle plan -t dev
databricks bundle deploy -t dev
databricks bundle run -t dev my_job
```

CLI behavior evolves; confirm available commands and flags for your installed version.

## CI/CD guardrails

- authenticate CI with a workload identity/service principal, not a personal token
- protect production targets with approvals and branch rules
- validate and test before deployment
- separate deploy permission from routine development
- record artifact/code revision and deployed resource state
- avoid embedding workspace URLs, secrets, or account IDs in source
- deploy the same reviewed revision across environments

## Testing pyramid

- Pure unit tests for transformations and business rules
- Contract tests for schemas and data quality
- Small integration tests in an isolated catalog/schema
- Post-deploy smoke tests for resources and permissions
- End-to-end tests only for critical flows

## Rollback

Resource rollback and data rollback are different. Re-deploying earlier code does not automatically undo table mutations. Plan compatibility, reversible schema changes, and compensating data operations separately.

## Official reference

- [Declarative Automation Bundles](https://docs.databricks.com/aws/en/dev-tools/bundles)

Related: [[Lakeflow Jobs and Orchestration]], [[Security and Production Guardrails]].
