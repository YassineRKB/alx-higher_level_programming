#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    bint = None
    lastkey = None
    for key in a_dictionary.keys():
        if bint is None:
            bint = a_dictionary[key]
            lastkey = key
        if bint < a_dictionary[key]:
            lastkey = key
            bint = a_dictionary[key]
    return lastkey
