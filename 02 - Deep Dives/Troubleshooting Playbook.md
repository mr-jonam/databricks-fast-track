---
title: Troubleshooting Playbook
aliases: [Databricks Troubleshooting]
tags: [databricks, troubleshooting, operations, deep-dive]
difficulty: intermediate
estimated_time: 30 minutes
updated: 2026-09-22
---

# Troubleshooting Playbook

## Evidence-first loop

1. State the expected and actual outcome.
2. Bound the first bad time, run, table version, or code revision.
3. Identify the failing layer: access, compute, code, data, storage, orchestration, or downstream.
4. Capture the smallest decisive evidence.
5. Test one hypothesis at a time on safe scope.
6. Fix, verify the business outcome, and record prevention.

## Fast triage

| Symptom | First evidence | Common causes |
|---|---|---|
| Permission denied | full object name, principal, grants, compute access mode | missing `USE`, wrong identity, workspace binding |
| Query slow | query profile, bytes/files scanned, exchanges, skew | full scan, poor join, small files, data skew |
| Job fails intermittently | task timeline, retry pattern, external errors | rate limit, transient service, concurrency |
| Wrong row count | source/target counts by key/date, join cardinality | duplicates, many-to-many join, late data |
| Streaming backlog | input/processing rate, batch duration, state size | source spike, state growth, slow sink |
| Schema failure | incoming schema, table schema, rescued fields | source drift, unsafe evolution, type conflict |
| High cost | usage by job/tag/SKU, runtime, retries | idle compute, full scans, duplicate work |

## Correctness before performance

Do not “fix” a timeout by changing join logic or dropping checks without reconciling output. Make the smallest safe reproduction, preserve failing input identifiers, and compare results to a known invariant.

## Spark evidence

- `df.explain("formatted")`
- SQL query profile
- Spark UI stages/tasks where available
- scan size and file count
- shuffle read/write, spill, skew, executor loss

## Delta evidence

```sql
DESCRIBE HISTORY catalog.schema.table;
DESCRIBE DETAIL catalog.schema.table;
```

Compare the first bad table version to the preceding version and the producing run/code revision.

## Permission sequence

Verify the actual run identity, then catalog use, schema use, object privilege, compute/access mode, and storage/external-location permissions. Admin success does not prove user access works.

## After the fix

- verify data and SLA, not only a green run
- add a regression test or monitor
- document trigger, root cause, contributing factors, and prevention
- remove temporary debug access and compute

Related: [[Monitoring and System Tables]], [[Decision Trees]].
