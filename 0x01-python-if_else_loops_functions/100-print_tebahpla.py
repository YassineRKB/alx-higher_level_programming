#!/usr/bin/python3
flag = -1
for i in range(122, 96, -1):
    if flag > 0:
        r = i - 32
    else:
        r = i
    print("{}".format(chr(r)), end="")
    flag = -1 * flag
