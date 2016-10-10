# Copying hdfs-site.xml on each node
sudo cat hdfs-site.xml >> $HADOOP_CONF_DIR/hdfs-site.xml

# Creating directory in the hadoop data node
sudo mkdir -p $HADOOP_HOME/data/hdfs/datanode

# Change the owner of the directory
sudo chown -R ubuntu $HADOOP_HOME
