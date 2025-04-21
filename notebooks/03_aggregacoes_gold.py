df = spark.read.format("delta").load("/mnt/silver/distribuicao")

df.groupBy("UF", "TIPO")   .sum("QUANTIDADE", "VALOR")   .write.format("delta").mode("overwrite")   .save("/mnt/gold/distribuicao_aggregado")