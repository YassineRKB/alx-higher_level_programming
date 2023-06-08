#!/usr/bin/python3
myadd = __import__("add_0.py").add()
a = 1
b = 2
r = myadd(a, b)
print("{:d} + {:d} = {:d}".format(a, b, r))
