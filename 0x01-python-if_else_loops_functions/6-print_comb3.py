#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if a < b:
            r = ((a * 10) + b)
            if r != 89:
                print("{:02d}".format(r), end=", ")
            else:
                print(r)
