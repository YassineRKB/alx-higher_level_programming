#!/usr/bin/python3
"""PPython script that takes your GitHub credentials
(username and password) and uses the GitHub API to
display your id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    HBAUTH = HTTPBasicAuth(sys.rgv[1], sys.argv[2])
    res = requests.get(
        'https://api.github.com/user',
        auth=HBAUTH
    )
    print(res.json().get('id'))
