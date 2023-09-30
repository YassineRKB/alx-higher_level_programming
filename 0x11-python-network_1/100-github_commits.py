#!/usr/bin/python3
"""Python script that takes 2 arguments
in order to solve this challenge."""
import requests
from sys import argv

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    commits = requests.get(url)
    for commit in commits.json()[:10]:
        sha = commit.get('sha')
        na = commit.get('commit').get('author').get('name')
        print(f"{sha}: {na}")
