#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    strf = ""
    for c in str:
        if i != n:
            strf[i] = c
        i += 1
    print("{}".format(strf))
