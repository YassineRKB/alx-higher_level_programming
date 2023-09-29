#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""
import urllib.request
import urllib.error
import sys
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            data = res.read().decode("utf-8")
            print(data)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
