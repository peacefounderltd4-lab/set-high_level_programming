#!/bin/bash
curl -s -L -w "%{http_code}" -o /tmp/body "$1" | grep -q '^200$' && cat /tmp/body
rm -f /tmp/body
