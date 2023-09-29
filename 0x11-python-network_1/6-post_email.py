#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the
URL and displays the value of the variable X-Request-Id in
the response header"""
import sys
import requests

if __name__ == "__main__":
    url = argv[1]
    json = {'email': sys.argv[2]}
    data = requests.post(url, data=json)
    print(data.text)
