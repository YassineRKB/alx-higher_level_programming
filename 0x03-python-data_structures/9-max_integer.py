#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    mint = 0
    for i in my_list:
        if i > mint:
            mint = i
    return mint
