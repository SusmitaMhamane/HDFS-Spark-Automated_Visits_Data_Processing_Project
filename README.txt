--Author: Susmita Mhamane
--Date: July 8, 2024

--Description
This project focuses on processing and analyzing visit records using Apache Spark and Hadoop. The primary objectives are to manage the data lifecycle by handling file operations and performing data transformations using Spark. The workflow includes checking for and removing an existing file on HDFS, uploading a new data file, and executing a Spark job to filter and transform the visit records based on specific criteria. This project demonstrates fundamental data manipulation techniques using Spark’s RDD API to efficiently process large datasets.

---------------------------------------------------------
Title: Visits Data Processing Project

Project Structure:
visits.sh: Shell script for managing files (checking, deleting, uploading) and executing the Spark job.
visits.py: Python script for processing data with Spark, including filtering and transforming records.
unset_jupyter.sh: Script for unsetting Jupyter-related environment variables, if necessary.
visits.txt: Sample data file in CSV format with visit records.
Prerequisites
Ensure the following are installed and configured:

---------------------------------------------------------

Apache Spark
Hadoop (HDFS)
Python with PySpark

---------------------------------------------------------

Instructions:
1. Prepare the Environment
If using Jupyter, unset the necessary environment variables using the unset_jupyter.sh script.

2. Run the Shell Script
Execute the visits.sh script to:

Check if the visits.txt file exists on HDFS and remove it if necessary.
Upload the new visits.txt file to HDFS.
Submit the Spark job defined in visits.py.
3. Spark Job Execution
The visits.py script will:

Initialize a Spark session.
Read the visits.txt file from HDFS.
Filter and transform the data based on specific criteria.
Print the count and details of the processed records.
Sample Data
The visits.txt file includes visit records in CSV format with various fields such as names, arrival times, appointment times, locations, and comments.

---------------------------------------------------------

Notes:
Verify that Spark and Hadoop are properly configured in your environment.
Adjust the file paths in the scripts to match your setup.
Test the scripts in a development environment before deploying them.
Troubleshooting
If issues arise:

Check Spark and Hadoop logs for detailed error messages.
Ensure the HDFS paths and file accessibility are correct.
Confirm that visits.txt is formatted properly.