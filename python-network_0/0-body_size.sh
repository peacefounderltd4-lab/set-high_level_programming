#!/bin/bash
# Display the response body size in bytes
curl -s "$1" | wc -c
