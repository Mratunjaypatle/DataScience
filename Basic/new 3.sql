| player_id | player_name  | team     | match_id | runs |
| --------: | ------------ | -------- | -------: | ---: |
|         1 | Virat Kohli  | India    |       M1 |   80 |
|         2 | Rohit Sharma | India    |       M1 |   60 |
|         3 | Virat Kohli  | India    |       M2 |   40 |
|         4 | Rohit Sharma | India    |       M2 |   90 |
|         5 | Shubman Gill | India    |       M1 |  100 |
|         6 | Babar Azam   | Pakistan |       M1 |   70 |
|         7 | Rizwan       | Pakistan |       M1 |   60 |
|         8 | Babar Azam   | Pakistan |       M2 |   50 |
|         9 | Rizwan       | Pakistan |       M2 |  100 |
|        10 | Fakhar Zaman | Pakistan |       M1 |  120 |

Find the top 2 players from each team based on their total runs across all matches.

with player_total as(
select player_name,team,,sum(runs) as total_runs
				from players
				group by player_name,team
				),
ranked_players as(
					select 
							player_name,
							team,
							total_runs,
							row_number() over(partition by team order by total_runs desc)
							as rn
							from player_total
							)
select player_name,team,total_runs from ranked_players
where rn < 2
order by team,total_runs desc;
===============================================================================	df = spark.read.format("delta").load(path)

df = df.withColumn(
    "amount",
    col("amount").cast("double")
)

df = df.filter(col("status") == "SUCCESS")

df = df.select(
    "customer_id",
    "transaction_date",
    "amount"
)

df.show()

##

df=(df.filter(col("status") = = "SUCCESS")
.select ("customer_id",
		"transaction_date",col("amount").cast("double").alias("amounts")
		)
		)
--action
				