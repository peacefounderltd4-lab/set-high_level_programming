#!/bin/bash
# Send a JSON file in the POST request body
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
