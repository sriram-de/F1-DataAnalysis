# Databricks notebook source
# MAGIC %md
# MAGIC #####explore the capabilities of dbutils.secrets.utility

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list(scope='formula1-scope')

# COMMAND ----------

dbutils.secrets.get(scope='formula1-scope',key='formula1dl-account-key')

# COMMAND ----------

display(df)

# COMMAND ----------

