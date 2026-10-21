#!/bin/bash
# Display only the HTTP status code
curl -s -o /dev/null -w "%{http_code}" "$1"
