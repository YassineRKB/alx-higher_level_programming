#!/usr/bin/python3
"""PPython script that takes your GitHub credentials
(username and password) and uses the GitHub API to
display your id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    res = requests.get(
        'https://api.github.com/user',
        auth=HTTPBasicAuth(sys.rgv[1], sys.argv[2])
    )
    print(res.json().get('id'))
