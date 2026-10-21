#!/bin/bash
# Send the required X-School-User-Id header
curl -s -H "X-School-User-Id: 98" "$1"
