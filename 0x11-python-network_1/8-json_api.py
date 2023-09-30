#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]
    req = {'q': letter}
    data = requests.post(url, data=req)

    try:
        data_dic = data.json()
        if data_dic:
            print(f"[{data_dic.get('id')}] {data_dic.get('name')}")
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
