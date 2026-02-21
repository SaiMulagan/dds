from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("YelpAnalytics") \
    .getOrCreate()

df = spark.read.json("gs://msds697_les_buckettes_du_yelp/Yelp_JSON/yelp_dataset/yelp_academic_dataset_business.json")

df.createOrReplaceTempView("business")

city_df = spark.sql("""
SELECT city,
       COUNT(*) as business_count,
       AVG(stars) as avg_stars
FROM business
GROUP BY city
ORDER BY business_count DESC
""")

city_df.show(10)