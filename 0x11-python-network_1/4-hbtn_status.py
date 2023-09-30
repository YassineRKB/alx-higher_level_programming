#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    data = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
