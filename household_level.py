import polars as pl
import numpy as np

fake_users_df = pl.read_csv("fake_users.csv")

household_df = fake_users_df.group_by("household_id").agg([
    pl.count("person").alias("household_size"),
    pl.mean("age").alias("mean_age"),
    pl.max("age").alias("max_age"),
    pl.min("age").alias("min_age"),
    pl.mean("income").alias("mean_income"),
    pl.max("income").alias("max_income"),
    pl.min("income").alias("min_income"),
    pl.sum("female").alias("no_females"),
    pl.col("female").sort_by("income").last().alias("female_main_earner"),
    (pl.col("age")<18).sum().alias("no_children")
])

household_df.write_csv("household_level_data.csv")
 