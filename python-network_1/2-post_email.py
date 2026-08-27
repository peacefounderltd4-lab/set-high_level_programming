#!/usr/bin/python3
"""Send an email using a POST request."""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    data = urllib.parse.urlencode({
        "email": sys.argv[2]
    }).encode("utf-8")

    with urllib.request.urlopen(sys.argv[1], data=data) as response:
        print(response.read().decode("utf-8"))
