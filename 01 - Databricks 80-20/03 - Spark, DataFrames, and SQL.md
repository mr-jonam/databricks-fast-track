---
title: Spark, DataFrames, and SQL
aliases: [Spark and SQL Essentials, PySpark Essentials]
tags: [databricks, apache-spark, sql, pyspark, beginner]
difficulty: beginner
estimated_time: 45 minutes
updated: 2026-09-22
---

# Spark, DataFrames, and SQL

## The useful Spark model

Spark builds a plan lazily, then executes it when an **action** needs a result. Transformations such as `select`, `filter`, and `groupBy` create a new DataFrame; actions such as `display`, `count`, `collect`, or writes execute work.

You do not need RDD internals to be productive. Learn DataFrames, SQL, plans, shuffles, and file layout first.

## Same transformation, two interfaces

SQL:

```sql
SELECT pickup_zip,
       COUNT(*) AS trip_count,
       ROUND(AVG(fare_amount), 2) AS avg_fare
FROM main.training.trips
WHERE trip_date >= DATE '2026-01-01'
GROUP BY pickup_zip
ORDER BY trip_count DESC;
```

PySpark:

```python
from pyspark.sql import functions as F

result = (
    spark.table("main.training.trips")
    .where(F.col("trip_date") >= F.lit("2026-01-01"))
    .groupBy("pickup_zip")
    .agg(
        F.count("*").alias("trip_count"),
        F.round(F.avg("fare_amount"), 2).alias("avg_fare"),
    )
    .orderBy(F.col("trip_count").desc())
)
```

Both produce logical plans for Spark. Choose the interface that keeps logic clearest and most testable.

## The performance model in five rules

1. Select only the columns you use.
2. Filter early so fewer rows move.
3. Joins and aggregations often cause network shuffles; inspect them.
4. Avoid `collect()` for data that does not safely fit on the driver.
5. Use built-in functions before Python UDFs; the engine can optimize built-ins.

## Join discipline

Before a join, answer:

- Is the key unique on either side?
- Can nulls appear?
- What row count do you expect afterward?
- Is one side genuinely small enough for a broadcast decision?

Validate instead of assuming:

```sql
SELECT customer_id, COUNT(*) AS n
FROM main.training.customers
GROUP BY customer_id
HAVING COUNT(*) > 1;
```

## Tips

- `display(df)` is for interactive inspection; writes or assertions are production outcomes.
- `df.explain("formatted")` and the SQL query profile reveal scans, exchanges, and skew.
- Do not cache by reflex. Cache only reused, expensive intermediate results and unpersist them.
- Avoid row-by-row loops over distributed data.

## Checkpoint

Why might a simple `groupBy` be expensive? Rows with the same key must be brought together, usually requiring a shuffle.

Next: [[04 - Delta Lake Essentials]]. Keep [[PySpark Cheatsheet]] and [[SQL Cheatsheet]] nearby.
