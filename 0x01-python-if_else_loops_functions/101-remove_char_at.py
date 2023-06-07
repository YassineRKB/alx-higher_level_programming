#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    slen = len(str)
    strf = ""
    while (i != slen):
        if i != n:
            strf += str[i]
        i += 1
    return strf
