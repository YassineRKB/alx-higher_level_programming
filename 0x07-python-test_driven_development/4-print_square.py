#!/usr/bin/python3
def print_square(size):
    TypeSize = isinstance(size, int)
    Valmsg = "size must be >= 0"
    errmsg = "size must be an integer"
    if not TypeSize:
        raise TypeError(errmsg)
    if size < 0:
        raise ValueError(Valmsg)
    if size != 0:
        for row in range(size):
            for column in range(size):
                print("#", end="")
            print()
    else:
        print("", end="")
