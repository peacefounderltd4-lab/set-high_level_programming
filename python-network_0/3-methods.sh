#!/bin/bash
curl -s -I -X OPTIONS "$1" | grep -i '^Allow:' | cut -d' ' -f2-
