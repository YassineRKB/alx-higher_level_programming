#!/usr/bin/python3
def multiple_returns(sentence):
    slen = len(sentence)
    if slen == 0:
        fchar = None
    else:
        fchar = sentence[0]
    res = (slen, fchar)
    return res
