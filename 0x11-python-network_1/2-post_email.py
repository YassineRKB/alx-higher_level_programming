#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter, and displays the
body of the response (decoded in utf-8)"""
import urllib.request as quest
from sys import argv

if __name__ == "__main__":
    mail = {"email": argv[2]}
    encoding = quest.parse.urlencode(mail).encode("ascii")
    req = quest.Request(argv[1], encoding)
    with quest.urlopen(req) as res:
        print(res.read().decode('utf8'))
