# Databricks notebook source
# MAGIC %md
# MAGIC ###Access Azure data lake using access keys
# MAGIC ####1.set the spark config.fs.account.key
# MAGIC ####2.list files from demo container
# MAGIC ####3.read data from circuits.csv file
# MAGIC

# COMMAND ----------

formula1dl_account_key=dbutils.secrets.get(scope='formula1-scope',key='formula1dl-account-key')

# COMMAND ----------

spark.conf.set("fs.azure.account.key.form1dl.dfs.core.windows.net",
formula1dl_account_key)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@form1dl.dfs.core.windows.net"))

# COMMAND ----------

df=spark.read.csv("abfss://demo@form1dl.dfs.core.windows.net/circuits.csv")

# COMMAND ----------

display(df)

# COMMAND ----------

