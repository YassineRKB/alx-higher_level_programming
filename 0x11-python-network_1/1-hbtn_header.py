#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response."""
import urllib.request as quest
from sys import argv

if __name__ == "__main__":
    req = quest.Request(argv[1])
    with quest.urlopen(req) as res:
        data = res.getheader('X-Request-Id')
        print(data)