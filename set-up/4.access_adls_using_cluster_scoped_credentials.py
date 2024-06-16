# Databricks notebook source
# MAGIC %md
# MAGIC ###Access Azure data lake using Sas
# MAGIC ######1.register azure ad application/service principal
# MAGIC ######2.generate secret/password for the application
# MAGIC ######3.set spark config with App/Client Id, Directory/ tenant Id & Secret
# MAGIC ######4.Assign role storage blob data contributor to the data lake
# MAGIC

# COMMAND ----------

client_id="5e69b6be-9829-4f52-bc3a-8ffd4b1ba75b"
tenant_id="ada668fb-a47b-4bed-b4c9-f0a9fc26f3e7"
client_secret="vV~8Q~Viy4O1.bqmjSF1-oFEMFKTSTgoA6lFMdcP"

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.form1dl.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.form1dl.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.form1dl.dfs.core.windows.net", client_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.form1dl.dfs.core.windows.net", client_secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.form1dl.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@form1dl.dfs.core.windows.net"))

# COMMAND ----------

df=spark.read.csv("abfss://demo@form1dl.dfs.core.windows.net/circuits.csv")

# COMMAND ----------

display(df)

# COMMAND ----------

