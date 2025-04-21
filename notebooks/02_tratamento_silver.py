from pyspark.sql.functions import to_date, trim, col

df = spark.read.format("delta").load("/mnt/bronze/distribuicao")

df_silver = df     .withColumn("DATA", to_date(col("DATA"), "yyyy/MM/dd"))     .withColumn("DATADEENTREGA", to_date(col("DATADEENTREGA"), "yyyy/MM/dd"))     .withColumn("UF", trim(col("UF")))

df_silver.write.format("delta").mode("overwrite").save("/mnt/silver/distribuicao")