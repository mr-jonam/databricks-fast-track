---
title: Lab 02 - SQL and PySpark Equivalence
aliases: [SQL PySpark Lab]
tags: [databricks, lab, sql, pyspark, beginner]
difficulty: beginner
estimated_time: 35 minutes
updated: 2026-09-22
---

# Lab 02: SQL and PySpark Equivalence

## Goal

Implement the same transformation in SQL and PySpark, then compare results and plans.

## Dataset

Use `samples.nyctaxi.trips` if available, or any table with categorical, numeric, and timestamp columns.

## Tasks

1. Filter to a bounded date range.
2. Group by one categorical field.
3. Calculate count, average amount, and maximum amount.
4. Sort by count descending and return the top 20.
5. Implement with SQL and DataFrames.
6. Compare row counts and a deterministic checksum/aggregate.
7. inspect `EXPLAIN FORMATTED` and `df.explain("formatted")`.

## Questions

- Do both plans scan the same columns and rows?
- Where does a shuffle occur?
- Does either interface make the business rule clearer?
- Did any implicit cast or null behavior differ?

## Bonus

Introduce a small dimension table, validate its key uniqueness, join it, and confirm that the output grain remains unchanged.

Related: [[03 - Spark, DataFrames, and SQL]], [[PySpark Cheatsheet]], [[SQL Cheatsheet]].
