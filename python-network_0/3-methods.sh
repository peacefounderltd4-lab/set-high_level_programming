#!/bin/bash
curl -s -I -X OPTIONS "$1" | grep -i '^Allow:' | sed 's/^[^:]*: *//' | tr -d '\r'
