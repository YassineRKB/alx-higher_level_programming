#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    ncset = set_1.union(set_2).difference(set_2 & set_1)
    
    return ncset
