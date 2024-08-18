#!/usr/bin/python
#
# Author: Susmita Vikas Mhamane
# Date: July 8, 2024

from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("Spark SQL basic example").enableHiveSupport().getOrCreate()
sc = spark.sparkContext

# Read visits.txt from HDFS
visits_rdd = sc.textFile("/user/talentum/visits.txt")
print(visits_rdd.count())

# Define function to filter POTUS visits
def filter_potus_visit(line):
    fields = line.split(',')
    return fields[19].strip() == 'POTUS'

# Apply filter to get RDD of POTUS visits
potus_rdd = visits_rdd.filter(filter_potus_visit)

# Define function to transform each record
def transform_record(record):
    fields = record.split(',')
    return (
        fields[0],  # lname
        fields[1],  # fname
        fields[6],  # time_of_arrival
        fields[11], # appt_scheduled_time
        fields[21], # location
        fields[25]  # comment
    )

# Apply transformation to get RDD of transformed POTUS visits
projected_potus_rdd = potus_rdd.map(transform_record)
print(projected_potus_rdd.count())

# Collect and print the transformed RDD for verification
results = projected_potus_rdd.collect()
for result in results:
    print(result)

# Stop Spark session
spark.stop()

