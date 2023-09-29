#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""
import urllib.request as quest
import urllib.error as questerr
from sys import argv

if __name__ == "__main__":
    try:
        with quest.urlopen(argv[1]) as res:
            data = res.read().decode("utf-8")
            print(data)
    except questerr.HTTPError as error:
        print("Error code: {}".format(error.code))
