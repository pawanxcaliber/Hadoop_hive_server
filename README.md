[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/big-data-europe/Lobby)

# About

This is an fork of official Hadoop Europe GitHub repo, where i added addition python script solve the reserved port issue in Windows Operating System

# docker-hive

This is a docker container for Apache Hive 2.3.2. It is based on https://github.com/big-data-europe/docker-hadoop so check there for Hadoop configurations.
This deploys Hive and starts a hiveserver2 on port 10000.
Metastore is running with a connection to postgresql database.
The hive configuration is performed with HIVE_SITE_CONF_ variables (see hadoop-hive.env for an example).

To run Hive with postgresql metastore:
```
   python container_start.py
```
Run the script present in the directory 

## This is a fork of docker-hive from Big-Data Europe 

Check out their repo
https://github.com/big-data-europe/docker-hive 
https://github.com/big-data-europe
