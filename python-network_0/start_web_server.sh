#!/bin/bash
# Start the selected local web server
VERSION="${1:-0}"
exec python3 "web_${VERSION}.py"
