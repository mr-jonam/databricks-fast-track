# Databricks notebook source
# MAGIC %md
# MAGIC # PySpark transformations with explicit quality checks

# COMMAND ----------

from pyspark.sql import Window
from pyspark.sql import functions as F


source = spark.table("main.training.bronze_orders")

typed = source.select(
    F.col("order_id").cast("long").alias("order_id"),
    F.col("order_ts").cast("timestamp").alias("order_ts"),
    F.col("amount").cast("decimal(12,2)").alias("amount"),
    F.col("ingestion_ts").cast("timestamp").alias("ingestion_ts"),
    "source_file",
)

valid = typed.where(F.col("order_id").isNotNull() & (F.col("amount") >= 0))

latest_first = Window.partitionBy("order_id").orderBy(F.col("ingestion_ts").desc())
silver = (
    valid.withColumn("row_number", F.row_number().over(latest_first))
    .where(F.col("row_number") == 1)
    .drop("row_number")
)

assert silver.where(F.col("order_id").isNull()).limit(1).count() == 0

(
    silver.write.mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("main.training.silver_orders_pyspark")
)

# COMMAND ----------

daily = (
    silver.groupBy(F.to_date("order_ts").alias("order_date"))
    .agg(
        F.count("*").alias("orders"),
        F.sum("amount").alias("revenue"),
    )
    .orderBy("order_date")
)

display(daily)
daily.explain("formatted")
