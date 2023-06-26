#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = 0
    try:
        res = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: " + str(e) + '\n')
        sys.stderr.flush()
        res = None
    return res
