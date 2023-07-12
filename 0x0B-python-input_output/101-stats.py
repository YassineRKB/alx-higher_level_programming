#!/usr/bin/python3
"""Module stats"""


from sys import stdin


def do_print(stat, value):
    """func to print stat"""
    print("File size: {}".format(value))
    for co in sorted(stat):
        print("{}: {}".format(co, stat[co]))


codes = [
    '200', '301',
    '400', '401',
    '403', '404',
    '405', '500'
    ]
val = 0
status = {}
i = 0
try:
    for data in stdin:
        if i != 10:
            i += 1
        else:
            do_print(status, val)
            i = 1
        data = data.split()
        try:
            val += int(data[-1])
        except (IndexError, ValueError):
            pass
        try:
            if data[-2] in codes:
                if status.get(data[-2], -1) != -1:
                    status[data[-2]] += 1
                else:
                    status[data[-2]] = 1
        except IndexError:
            pass
    do_print(status, val)

except KeyboardInterrupt:
    do_print(status, val)
    raise
