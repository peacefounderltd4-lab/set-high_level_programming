#!/bin/bash
curl -s -o /tmp/body -w "%{http_code}" "$1" | grep -q "^200$" && cat /tmp/body
rm -f /tmp/body
