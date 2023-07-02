#!/usr/bin/python3
def add_integer(a, b=98):
    TypeA = isinstance(a, (float, int))
    TypeB = isinstance(b, (float, int))
    msg = "a must be an integer" if not TypeA else "b must be an integer"
    if not TypeA or not TypeB:
        raise TypeError(msg)
    return int(a) + int(b)
