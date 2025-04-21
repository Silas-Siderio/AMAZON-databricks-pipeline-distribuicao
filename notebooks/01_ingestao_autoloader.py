from pyspark.sql.functions import input_file_name

df = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "json")
    .load("/mnt/raw/distribuicao")
)

df.withColumn("source_file", input_file_name())   .writeStream.format("delta")   .option("checkpointLocation", "/mnt/checkpoints/bronze/distribuicao")   .option("path", "/mnt/bronze/distribuicao")   .outputMode("append")   .start()