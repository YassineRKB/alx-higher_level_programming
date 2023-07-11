#!/usr/bin/python3
"""Module for read_file"""


def read_file(filename=""):
    """func to read text file"""
    with open(filename, "r") as r:
        print(r.read(), end="")
