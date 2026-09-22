# Lakeflow pipeline source file. Configure the target catalog and schema in the pipeline.

from pyspark import pipelines as dp
from pyspark.sql import functions as F


@dp.table(name="bronze_orders_stream")
def bronze_orders_stream():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load("/Volumes/main/training/landing/orders")
        .withColumn("ingestion_ts", F.current_timestamp())
    )


@dp.materialized_view(name="valid_orders")
def valid_orders():
    return (
        spark.read.table("bronze_orders_stream")
        .where(F.col("order_id").isNotNull() & (F.col("amount") >= 0))
    )


@dp.materialized_view(name="daily_revenue")
def daily_revenue():
    return (
        spark.read.table("valid_orders")
        .groupBy(F.to_date("order_ts").alias("order_date"))
        .agg(F.sum("amount").alias("revenue"))
    )
