#!/usr/bin/python3
"""PPython script that takes your GitHub credentials
(username and password) and uses the GitHub API to
display your id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    URL = 'https://api.github.com/user'
    res = requests.get(URL, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(res.json().get('id'))
