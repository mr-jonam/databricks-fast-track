# Databricks notebook source
# MAGIC %md
# MAGIC # Auto Loader baseline
# MAGIC Update paths and permissions before running. Use unique checkpoints.

# COMMAND ----------

source_path = "/Volumes/main/training/landing/orders"
schema_path = "/Volumes/main/training/checkpoints/orders_schema"
checkpoint_path = "/Volumes/main/training/checkpoints/orders_bronze"

orders = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.schemaLocation", schema_path)
    .option("cloudFiles.schemaEvolutionMode", "addNewColumns")
    .load(source_path)
)

query = (
    orders.writeStream.option("checkpointLocation", checkpoint_path)
    .trigger(availableNow=True)
    .toTable("main.training.bronze_orders_stream")
)

query.awaitTermination()
