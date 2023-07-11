#!/usr/bin/python3
"""Module for load_from_json_file"""
import json


def load_from_json_file(filename):
    """func to read obj from file in json format"""
    with open(filename, "r") as r:
        return (json.loads(r.read()))
