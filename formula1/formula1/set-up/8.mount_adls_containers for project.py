# Databricks notebook source
# MAGIC %md
# MAGIC ###Mount Dl using service principal
# MAGIC #####1.get client_id,tenant_id,client_secret from key vault
# MAGIC #####2.set spark config with app/client id,directory/tenant & secret
# MAGIC #####3. call file system utility mount to mount the storage
# MAGIC #####4. Explore other file system utilities related to mount
# MAGIC

# COMMAND ----------

def mount_adls(storage_account_name,container_name):
    client_id=dbutils.secrets.get(scope='formula1-scope',key='formula1dl-client-id')
    tenant_id=dbutils.secrets.get(scope='formula1-scope',key='formula1dl-tenant-id')
    client_secret=dbutils.secrets.get(scope='formula1-scope',key='formula1dl-client-secret')

    configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id,
          "fs.azure.account.oauth2.client.secret": client_secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}
    if any(mount.mountPoint == f"/mnt/{storage_account_name}/{container_name}" for mount in dbutils.fs.mounts()):
        dbutils.fs.unmount(f"/mnt/{storage_account_name}/{container_name}")

    dbutils.fs.mount(
    source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_account_name}/{container_name}",
    extra_configs = configs)

    display(dbutils.fs.mounts())




# COMMAND ----------

mount_adls('form1dl','raw')
mount_adls('form1dl','presentation')
mount_adls('form1dl','processed')

# COMMAND ----------



# COMMAND ----------

client_id=dbutils.secrets.get(scope='formula1-scope',key='formula1dl-client-id')
tenant_id=dbutils.secrets.get(scope='formula1-scope',key='formula1dl-tenant-id')
client_secret=dbutils.secrets.get(scope='formula1-scope',key='formula1dl-client-secret')




# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id,
          "fs.azure.account.oauth2.client.secret": client_secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

# COMMAND ----------



dbutils.fs.mount(
  source = "abfss://demo@form1dl.dfs.core.windows.net/",
  mount_point = "/mnt/form1dl/demo",
  extra_configs = configs)

# COMMAND ----------

display(dbutils.fs.ls("/mnt/form1dl/demo/circuits.csv"))

# COMMAND ----------

df=spark.read.csv("/mnt/form1dl/demo/circuits.csv")

# COMMAND ----------

display(df)

# COMMAND ----------

dbutils.fs.unmount()

# COMMAND ----------

