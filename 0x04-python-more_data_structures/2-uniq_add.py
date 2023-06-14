#!/usr/bin/python3
def uniq_add(my_list=[]):
    doset = set(my_list)
    result = 0
    for i in doset:
        result += sum(int(i))
    return result
