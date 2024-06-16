# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE DATABASE f1_raw;

# COMMAND ----------

# MAGIC %md
# MAGIC #### Create tables for CSV files

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS f1_raw.circuits;
# MAGIC CREATE TABLE IF NOT EXISTS f1_raw.circuits(circuitId INT,
# MAGIC circuitRef STRING,
# MAGIC name STRING,
# MAGIC location STRING,
# MAGIC country STRING,
# MAGIC lat DOUBLE,
# MAGIC lng DOUBLE,
# MAGIC alt INT,
# MAGIC url STRING
# MAGIC )
# MAGIC USING csv
# MAGIC OPTIONS (path "/mnt/form1dl/raw/circuits.csv", header true)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Create races table

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS f1_raw.races;
# MAGIC CREATE TABLE IF NOT EXISTS f1_raw.races(raceId INT,
# MAGIC year INT,
# MAGIC round INT,
# MAGIC circuitId INT,
# MAGIC name STRING,
# MAGIC date DATE,
# MAGIC time STRING,
# MAGIC url STRING)
# MAGIC USING csv
# MAGIC OPTIONS (path "/mnt/form1dl/raw/races.csv", header true)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Create tables for JSON files
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Create constructors table
# MAGIC * Single Line JSON
# MAGIC * Simple structure

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS f1_raw.constructors;
# MAGIC CREATE TABLE IF NOT EXISTS f1_raw.constructors(
# MAGIC constructorId INT,
# MAGIC constructorRef STRING,
# MAGIC name STRING,
# MAGIC nationality STRING,
# MAGIC url STRING)
# MAGIC USING json
# MAGIC OPTIONS(path "/mnt/form1dl/raw/constructors.json")

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC ##### Create drivers table
# MAGIC * Single Line JSON
# MAGIC * Complex structure

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS f1_raw.drivers;
# MAGIC CREATE TABLE IF NOT EXISTS f1_raw.drivers(
# MAGIC driverId INT,
# MAGIC driverRef STRING,
# MAGIC number INT,
# MAGIC code STRING,
# MAGIC name STRUCT<forename: STRING, surname: STRING>,
# MAGIC dob DATE,
# MAGIC nationality STRING,
# MAGIC url STRING)
# MAGIC USING json
# MAGIC OPTIONS (path "/mnt/form1dl/raw/drivers.json")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Create results table
# MAGIC * Single Line JSON
# MAGIC * Simple structure

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS f1_raw.results;
# MAGIC CREATE TABLE IF NOT EXISTS f1_raw.results(
# MAGIC resultId INT,
# MAGIC raceId INT,
# MAGIC driverId INT,
# MAGIC constructorId INT,
# MAGIC number INT,grid INT,
# MAGIC position INT,
# MAGIC positionText STRING,
# MAGIC positionOrder INT,
# MAGIC points INT,
# MAGIC laps INT,
# MAGIC time STRING,
# MAGIC milliseconds INT,
# MAGIC fastestLap INT,
# MAGIC rank INT,
# MAGIC fastestLapTime STRING,
# MAGIC fastestLapSpeed FLOAT,
# MAGIC statusId STRING)
# MAGIC USING json
# MAGIC OPTIONS(path "/mnt/form1dl/raw/results.json")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Create pit stops table
# MAGIC * Multi Line JSON
# MAGIC * Simple structure

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS f1_raw.pit_stops;
# MAGIC CREATE TABLE IF NOT EXISTS f1_raw.pit_stops(
# MAGIC driverId INT,
# MAGIC duration STRING,
# MAGIC lap INT,
# MAGIC milliseconds INT,
# MAGIC raceId INT,
# MAGIC stop INT,
# MAGIC time STRING)
# MAGIC USING json
# MAGIC OPTIONS(path "/mnt/form1dl/raw/pit_stops.json", multiLine true)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Create tables for list of files
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Create Lap Times Table
# MAGIC * CSV file
# MAGIC * Multiple files

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS f1_raw.lap_times;
# MAGIC CREATE TABLE IF NOT EXISTS f1_raw.lap_times(
# MAGIC raceId INT,
# MAGIC driverId INT,
# MAGIC lap INT,
# MAGIC position INT,
# MAGIC time STRING,
# MAGIC milliseconds INT
# MAGIC )
# MAGIC USING csv
# MAGIC OPTIONS (path "/mnt/form1dl/raw/lap_times")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Create Qualifying Table
# MAGIC * JSON file
# MAGIC * MultiLine JSON
# MAGIC * Multiple files

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS f1_raw.qualifying;
# MAGIC CREATE TABLE IF NOT EXISTS f1_raw.qualifying(
# MAGIC constructorId INT,
# MAGIC driverId INT,
# MAGIC number INT,
# MAGIC position INT,
# MAGIC q1 STRING,
# MAGIC q2 STRING,
# MAGIC q3 STRING,
# MAGIC qualifyId INT,
# MAGIC raceId INT)
# MAGIC USING json
# MAGIC OPTIONS (path "/mnt/form1dl/raw/qualifying", multiLine true)

# COMMAND ----------

