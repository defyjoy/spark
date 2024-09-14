from pyspark.sql import SparkSession
import os
import glob

# from pyspark import SparkFiles

# spark = SparkSession.builder.appName('abc').getOrCreate()
spark = (SparkSession.builder
            .appName("myApp")
            .master("spark://localhost:7077")
            # .config("spark.master", "spark://localhost:7077")
            # .config("spark.sql.warehouse.dir")

            .getOrCreate()) ## Running in docker container

print(os.getcwd())
print(os.listdir())

df=(spark.read.format("csv")
      .option("recursiveFileLookup", "true")
      .option("pathGlobFilter","*.csv")
      .csv("/Volumes/Workhub/Personal/Datascience/Spark/data/world-championship-history/F1-History",header=True))
      # .load("dbfs:/FileStore/tables/A/",header=True))


# df=(spark.read.format("csv")
#       .option("recursiveFileLookup", "true")
#       .option("pathGlobFilter","*.csv")
#       .csv("/home/spark/data",header=True))
      # .csv("file:////Volumes/Workhub/Personal/Python/data/world-championship-history/F1-History",header=True))

# sc = spark.sparkContext

# df = sc.textFile(SparkFiles

#                  .get('Crimes.csv'))

# df.show()


# print("----------- count: %s",df.count())
# print(f"----------- count: {df.count()}",)

