#!/usr/bin/python3
"""Module append_after"""


def append_after(filename="", search_string="", new_string=""):
    """func to read file name and append after string search"""
    with open(filename, "r") as r:
        lines = r.readlines()
    with open(filename, "w") as w:
        for line in lines:
            w.write(line)
            if search_string in line:
                w.write(new_string)
