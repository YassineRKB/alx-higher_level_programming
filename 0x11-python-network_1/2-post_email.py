#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter, and displays the
body of the response (decoded in utf-8)"""
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    mail = {"email": sys.argv[2]}
    encoding = urllib.parse.urlencode(mail).encode("ascii")
    req = urllib.request.Request(sys.argv[1], encoding)
    with urllib.request.urlopen(req) as res:
        data = res.read().decode('utf8')
        print(data)
