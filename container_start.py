#!/usr/bin/env python3
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

# Set these as environment variables, so docker-compose picks them up
os.environ['NAMENODE_HOST_PORT'] = str(namenode_port)
os.environ['DATANODE_HOST_PORT'] = str(datanode_port)

print(f"Using ports:\n - Namenode: {namenode_port} -> container port 50070\n - Datanode: {datanode_port} -> container port 50075")

# Start docker-compose with the dynamically set environment variables
try:
    subprocess.check_call(["docker-compose", "up", "-d"])
    print("Services started successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error starting services: {e}")
