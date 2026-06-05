from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CloudGuardianETL") \
    .getOrCreate()

input_path = "s3://cloud-guardian/raw/"
output_path = "s3://cloud-guardian/processed/"

df = spark.read.json(input_path)

clean_df = df.dropDuplicates()

clean_df.write.mode("overwrite") \
    .parquet(output_path)

spark.stop()