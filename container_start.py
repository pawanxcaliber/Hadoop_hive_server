import socket
import os
import subprocess

def get_free_port():
    """Return an available port on the host."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))  # Let OS choose an available port
        return s.getsockname()[1]

# Retrieve free ports for each service needing dynamic host port mapping
namenode_port = get_free_port()
datanode_port = get_free_port()
hive_server_port = get_free_port()       # For Hive Server (container port 10000)
hive_metastore_port = get_free_port()     # For Hive Metastore (container port 9083)
presto_port = get_free_port()             # For Presto Coordinator (container port 8080)

# Set environment variables so docker-compose picks them up
os.environ['NAMENODE_HOST_PORT'] = str(namenode_port)
os.environ['DATANODE_HOST_PORT'] = str(datanode_port)
os.environ['HIVE_SERVER_HOST_PORT'] = str(hive_server_port)
os.environ['HIVE_METASTORE_HOST_PORT'] = str(hive_metastore_port)
os.environ['PRESTO_HOST_PORT'] = str(presto_port)

print(
    f"Using ports:\n"
    f" - Namenode: {namenode_port} -> container port 50070\n"
    f" - Datanode: {datanode_port} -> container port 50075\n"
    f" - Hive Server: {hive_server_port} -> container port 10000\n"
    f" - Hive Metastore: {hive_metastore_port} -> container port 9083\n"
    f" - Presto Coordinator: {presto_port} -> container port 8080"
)

# Start docker-compose with the dynamically set environment variables
try:
    subprocess.check_call(["docker-compose", "up", "-d"])
    print("Services started successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error starting services: {e}")
