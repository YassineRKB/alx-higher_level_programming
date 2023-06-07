#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    l = len(str)
    strf = ""
    while (i != l):
        if i != n:
            strf += str[i]
        i += 1
    return strf
