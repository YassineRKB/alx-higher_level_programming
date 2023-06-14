#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    avg = 0
    for i in my_list:
        avg = avg + (i[0] * i[1])
        total += i[1]
    avg = avg / total
    return avg
