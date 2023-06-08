#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    nargs = len(argv)
    if nargs != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] == "+":
        op = add
    elif argv[2] == "-":
        op = sub
    elif argv[2] == "*":
        op = mul
    elif argv[2] == "/":
        op = div
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    r = op(a, b)
    print("{} {} {} = {}".format(a, operator, b, r))
