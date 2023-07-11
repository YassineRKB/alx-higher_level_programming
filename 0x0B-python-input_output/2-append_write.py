#!/usr/bin/python3
"""Module for append_write"""


def append_write(filename="", text=""):
    """func to write text file"""
    with open(filename, "a") as r:
        return r.write(text)
