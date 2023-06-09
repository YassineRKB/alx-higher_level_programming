#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    verdict = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        sys.stderr.write("Exception: " + str(e) + '\n')
        sys.stderr.flush()
        verdict = False
    return verdict
