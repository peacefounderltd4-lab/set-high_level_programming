#!/usr/bin/python3
"""List the 10 most recent commits of a GitHub repository."""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1]
    )

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()

        for commit in commits[:10]:
            sha = commit.get("sha")
            author = commit.get("commit", {}).get("author", {})
            name = author.get("name")
            print("{}: {}".format(sha, name))
