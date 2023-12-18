#! /usr/bin/env bash

echo "Starting broadcast"
python3.11 -m pip install -r broadcast_requirements.txt
python3.11 broadcast.py
