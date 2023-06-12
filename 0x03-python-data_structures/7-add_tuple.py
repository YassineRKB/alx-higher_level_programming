#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    fint = 0
    sint = 0
    if len(tuple_a) == 0:
        fint += 0
    else:
        fint += tuple_a[0]

    if len(tuple_a) <= 1:
        sint += 0
    else:
        sint += tuple_a[1]

    if len(tuple_b) == 0:
        fint += 0
    else:
        fint += tuple_b[0]

    if len(tuple_b) <= 1:
        sint += 0
    else:
        sint += tuple_b[1]
    res = (fint, sint)
    return res
