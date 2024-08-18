#!/bin/bash
#
# Author: Susmita Vikas Mhamane
# Date: July 8, 2024

source ./unset_jupyter.sh
hdfs dfs -test -e /user/talentum/visits.txt
if [ $? -eq 0 ]; then
    echo "File is There"
    hdfs dfs -rm /user/talentum/visits.txt
    echo "File Deleted Successfully"
fi
echo "Putting file on HDFS."
hdfs dfs -put ~/shared/visits.txt /user/talentum/
echo "File Copied Successfully"

spark-submit visits.py
