#!/bin/bash
# Start the local test web server (use 0 or 1 to choose the response)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VERSION="${1:-0}"
if [ "$VERSION" = "1" ]; then
    exec python3 "$SCRIPT_DIR/web_1.py"
else
    exec python3 "$SCRIPT_DIR/web_0.py"
fi
