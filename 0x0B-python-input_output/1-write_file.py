#!/usr/bin/python3
"""Module for write_file"""


def write_file(filename="", text=""):
    """func to write text file"""
    with open(filename, "w") as r:
        return r.write(text)
