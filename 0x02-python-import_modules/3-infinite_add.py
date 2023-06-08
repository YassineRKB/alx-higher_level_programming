#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    nargs = len(argv)
    r = 0
    for i in range(1, nargs):
        r += int(argv[i])
    print(r)
