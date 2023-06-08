#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    nargs = len(argv)
    print("{} {}".format(nargs - 1, "argument"), end="")
    if nargs > 1:
        print({True: ":", False: "s:"}[nargs == 2])
        for i in range(1, nargs):
            print("{}: {}".format(i, argv[i]))
    else:
        print("s.")
