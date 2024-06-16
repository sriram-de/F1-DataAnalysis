# Databricks notebook source
html = """<h1 style="color:Black;text-align:center;font-family:Ariel">Report on Dominant Formula 1 Teams </h1>"""
displayHTML(html)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMP VIEW v_dominant_teams
# MAGIC AS
# MAGIC SELECT team_name,
# MAGIC        COUNT(1) AS total_races,
# MAGIC        SUM(calculated_points) AS total_points,
# MAGIC        AVG(calculated_points) AS avg_points,
# MAGIC        RANK() OVER(ORDER BY AVG(calculated_points) DESC) team_rank
# MAGIC   FROM f1_presentation.calculated_race_results
# MAGIC GROUP BY team_name
# MAGIC HAVING COUNT(1) >= 100
# MAGIC ORDER BY avg_points DESC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM v_dominant_teams;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT race_year, 
# MAGIC        team_name,
# MAGIC        COUNT(1) AS total_races,
# MAGIC        SUM(calculated_points) AS total_points,
# MAGIC        AVG(calculated_points) AS avg_points
# MAGIC   FROM f1_presentation.calculated_race_results
# MAGIC  WHERE team_name IN (SELECT team_name FROM v_dominant_teams WHERE team_rank <= 5)
# MAGIC GROUP BY race_year, team_name
# MAGIC ORDER BY race_year, avg_points DESC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT race_year, 
# MAGIC        team_name,
# MAGIC        COUNT(1) AS total_races,
# MAGIC        SUM(calculated_points) AS total_points,
# MAGIC        AVG(calculated_points) AS avg_points
# MAGIC   FROM f1_presentation.calculated_race_results
# MAGIC  WHERE team_name IN (SELECT team_name FROM v_dominant_teams WHERE team_rank <= 5)
# MAGIC GROUP BY race_year, team_name
# MAGIC ORDER BY race_year, avg_points DESC

# COMMAND ----------

