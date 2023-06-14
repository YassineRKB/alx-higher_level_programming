#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = dict()
    for key in a_dictionary.keys():
        value = a_dictionary[key] * 2
        dic.update({key: value})
    return dic
