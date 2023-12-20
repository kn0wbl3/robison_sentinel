#! /usr/bin/env bash

echo "Starting server"
python3.11 -m pip install -r server_requirements.txt
python3.11 server.py
