#!/bin/bash
body=$(mktemp)
status=$(curl -s -o "$body" -w "%{http_code}" "$1")
if [ "$status" = "200" ]; then
    cat "$body"
fi
rm -f "$body"
