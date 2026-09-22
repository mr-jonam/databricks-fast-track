---
title: Decision Trees
aliases: [Databricks Decisions]
tags: [databricks, decisions, architecture, reference]
difficulty: intermediate
estimated_time: 15 minutes
updated: 2026-09-22
---

# Decision Trees

## SQL or PySpark?

```text
Is the transformation naturally relational?
├─ Yes → Can the team express and test it clearly in SQL?
│  ├─ Yes → SQL
│  └─ No  → PySpark DataFrames
└─ No  → Do you need Python libraries/composition or ML logic?
   ├─ Yes → Python/PySpark
   └─ No  → Recheck whether built-in SQL/DataFrame functions solve it
```

## Job or Lakeflow pipeline?

```text
Are you declaring datasets and their incremental dependencies?
├─ Yes → Lakeflow pipeline
└─ No  → Are you coordinating heterogeneous tasks/control flow?
   ├─ Yes → Lakeflow Job
   └─ No  → A single scheduled query/task may be enough
```

A Job can orchestrate a pipeline; the choice is not exclusive.

## Batch or streaming?

```text
Is there a business latency requirement below the batch interval?
├─ No → Batch or triggered incremental
└─ Yes → Can source/sink and operations support streaming correctly?
   ├─ Yes → Streaming, with checkpoint/state/late-data design
   └─ No  → Negotiate latency or redesign dependencies
```

## Managed or external table?

```text
Must another platform independently control the files/lifecycle?
├─ No → Managed table
└─ Yes → External table, with explicit storage governance
```

## Serverless or classic compute?

```text
Is the workload supported on serverless in your cloud/region?
├─ Yes → Start serverless and measure
└─ No  → Classic compute with the least customization needed
```

## Optimize or scale?

```text
Is the query scanning/moving much more data than necessary?
├─ Yes → Fix query, join, or layout
└─ No  → Is SLA still unmet at realistic concurrency?
   ├─ Yes → Test scaling with cost comparison
   └─ No  → Keep current size
```

Related: [[Compute and Cost Control]], [[Lakeflow Pipelines]].
