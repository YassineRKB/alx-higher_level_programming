#!/usr/bin/python3
"""Module for save_to_json_file"""
import json


def save_to_json_file(obj, filename):
    """func to write obj to file in json format"""
    with open(filename, "w") as w:
        w.write(json.dumps(obj))
