---
title: PySpark Cheatsheet
aliases: [Spark DataFrame Cheatsheet]
tags: [databricks, pyspark, apache-spark, reference]
difficulty: beginner
estimated_time: 15 minutes
updated: 2026-09-22
---

# PySpark Cheatsheet

```python
from pyspark.sql import functions as F
from pyspark.sql import Window
```

## Read and inspect

```python
df = spark.table("main.training.orders")
df.printSchema()
display(df.limit(20))
df.explain("formatted")
```

## Select, filter, derive

```python
clean = (
    df.select("order_id", "customer_id", "order_ts", "amount")
    .where(F.col("order_id").isNotNull() & (F.col("amount") >= 0))
    .withColumn("order_date", F.to_date("order_ts"))
)
```

## Aggregate

```python
daily = (
    clean.groupBy("order_date")
    .agg(
        F.countDistinct("order_id").alias("orders"),
        F.sum("amount").alias("revenue"),
    )
)
```

## Deduplicate by latest event

```python
window = Window.partitionBy("order_id").orderBy(
    F.col("source_updated_at").desc(), F.col("ingestion_ts").desc()
)
latest = df.withColumn("rn", F.row_number().over(window)).where("rn = 1").drop("rn")
```

## Join with explicit cardinality thinking

```python
enriched = clean.join(
    spark.table("main.training.customers"),
    on="customer_id",
    how="left",
)
```

## Write

```python
(daily.write.mode("overwrite").saveAsTable("main.training.daily_revenue"))
```

Avoid unbounded `collect()`, Python UDFs when built-ins exist, and row-by-row loops. Use `F.broadcast()` only with evidence that the side is small enough.

Related: [[03 - Spark, DataFrames, and SQL]], [[Delta Lake Performance and Reliability]].
