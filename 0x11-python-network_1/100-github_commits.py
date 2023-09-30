#!/usr/bin/python3
"""Python script that takes 2 arguments
in order to solve this challenge."""
import sys
import requests

if __name__ == "__main__":
    URL = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[2]}/commits"
    req = requests.get(URL)
    totalcommits = req.json()
    for commit in totalcommits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
