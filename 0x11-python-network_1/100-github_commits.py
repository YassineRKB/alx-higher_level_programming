#!/usr/bin/python3
"""Python script that takes 2 arguments
in order to solve this challenge."""
import requests
from sys import argv

if __name__ == "__main__":
    URL = f"https://api.github.com/repos/{argv[2]}/{argv[2]}/commits"
    req = requests.get(URL)
    totalcommits = req.json()
    try:
        for commit in totalcommits[:10]:
            print(commit.get('sha'), end=': ')
            print(commit.get('commit').get('author').get('name'))
    except IndexError:
        pass
