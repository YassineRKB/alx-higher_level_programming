#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    verdict = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        sys.stderr.write("Exception: {}".format(e))
        verdict = False
        sys.stderr.flush()
    return verdict
