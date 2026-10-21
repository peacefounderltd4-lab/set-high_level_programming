#!/bin/bash
# Display the HTTP methods accepted by the server
curl -s -I -X OPTIONS "$1" | grep -i '^Allow:' | cut -d ' ' -f 2- | tr -d '\r'
