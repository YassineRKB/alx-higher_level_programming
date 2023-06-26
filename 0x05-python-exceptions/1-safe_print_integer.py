#!/usr/bin/python3
def safe_print_integer(value):
    verdict = True
    try:
        print("{:d}".format(value))
    except Exception:
        verdict = False
    return verdict
