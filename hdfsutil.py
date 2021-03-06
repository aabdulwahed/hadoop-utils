import os
import sys

	
def __generate_hdfs_site():	
	return """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
      <name>dfs.replication</name>
      <value>3</value>
    </property>
    <property>
      <name>dfs.name.dir</name>
      <value>/usr/local/hadoop/hdfs/name</value>
    </property>
    <property>
      <name>dfs.data.dir</name>
      <value>/usr/local/hadoop/hdfs/data</value>
    </property>
</configuration>
	"""
