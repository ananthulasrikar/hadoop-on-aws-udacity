# Copy the hosts file to /etc/hosts
sudo cat hosts-file >> /etc/hosts

# Creating directory on the name node
sudo mkdir -p $HADOOP_HOME/data/hdfs/namenode

# Changing the owner to ubuntu
sudo chown -R ubuntu $HADOOP_HOME

# Format name node & Start DFS
hdfs namenode -format
$HADOOP_HOME/sbin/start-dfs.sh

# start yarn
$HADOOP_HOME/sbin/start-yarn.sh

# start job history server
$HADOOP_HOME/sbin/mr-jobhistory-daemon.sh start historyserver

# To see java Heap process
jps

# Creating directories in HDFS
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/ubuntu
