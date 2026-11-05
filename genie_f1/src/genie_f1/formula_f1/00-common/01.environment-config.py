# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# Unity Catalog Object Names
catalog_name = 'formula1_incr'
bronze_schema = 'bronze'
silver_schema = 'silver'
gold_schema = 'gold'
control_schema = 'control'

# COMMAND ----------

landing_folder_path = '/Volumes/formula1_incr/landing/files'