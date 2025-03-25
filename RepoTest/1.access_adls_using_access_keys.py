# Databricks notebook source
gamesglobalaccountkey = dbutils.secrets.get(scope= "Gamesglobal-scope",key='adlsaccesskey')

# COMMAND ----------

spark.conf.set("fs.azure.account.key.devadlsgentwo.dfs.core.windows.net",gamesglobalaccountkey)

# COMMAND ----------

display(dbutils.fs.ls("abfss://gamesglobal@devadlsgentwo.dfs.core.windows.net"))

# COMMAND ----------

df = spark.read.option("multiline","true").json("abfss://gamesglobal@devadlsgentwo.dfs.core.windows.net/analytics.json")
