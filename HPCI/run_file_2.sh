#!/bin/bash
# run this first to give permissions to run the file: chmod +x run_file_2.sh

n=2
x="1a"
x2="1b"

# delete and create folder
hadoop fs -rm -r project$n
hadoop fs -mkdir -p /user/cs2375008/project$n/
# copy input data across
hadoop fs -copyFromLocal storms.csv /user/cs2375008/project$n/

# run first mapreduce job
hadoop jar /usr/local/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-files mapper2.py,reducer1.py \
-input project$n/storms.csv \
-output project$n/run$x/ \
-mapper "python mapper1.py" \
-reducer "python reducer1.py"
# check output
hadoop fs -ls /user/cs2375008/project$n/run$x/
# delete and copy output to linux
rm output$x.txt
hadoop fs -copyToLocal /user/cs2375008/project$n/run$x/part-00000 output$x.txt

# run second mapreduce job using the output of the first as input
hadoop jar /usr/local/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-files mapper2.py,reducer2.py \
-input project$n/run$x/ \
-output project$n/run$x2/ \
-mapper "python mapper2.py" \
-reducer "python reducer2.py"
# check output
hadoop fs -ls /user/cs2375008/project$n/run$x2/
# delete and copy output to linux
rm output$x2.txt
hadoop fs -copyToLocal /user/cs2375008/project$n/run$x2/part-00000 output$x2.txt

# view file
less -N output$x2.txt

# copy to local (run from local machine)
#scp cs2375008@134.83.83.28:/home/cs2375008/content/assignment/output1b.txt .