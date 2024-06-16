# Databricks notebook source
# MAGIC %md
# MAGIC ###Access Azure data lake using Sas
# MAGIC ####1.set the spark config.fs.account.key
# MAGIC ####2.list files from demo container
# MAGIC ####3.read data from circuits.csv file
# MAGIC

# COMMAND ----------

formula1dl_sas_token=dbutils.secrets.get(scope='formula1-scope',key='formula1dl-sas-token')

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.form1dl.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.form1dl.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.form1dl.dfs.core.windows.net", formula1dl_sas_token)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@form1dl.dfs.core.windows.net"))

# COMMAND ----------

df=spark.read.csv("abfss://demo@form1dl.dfs.core.windows.net/circuits.csv")

# COMMAND ----------

display(df)

# COMMAND ----------

