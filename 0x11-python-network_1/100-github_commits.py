#!/usr/bin/python3
"""Python script that takes 2 arguments
in order to solve this challenge."""
import sys
import requests

if __name__ == "__main__":
    owner = sys.argv[1]
    repo = sys.argv[2]
    URL = f"https://api.github.com/repos/{owner}/{repo}/commits"
    req = requests.get(URL)
    total_commits = req.json()
    for commit in total_commits[0:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")
