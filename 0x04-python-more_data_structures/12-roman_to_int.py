#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {'I': 1000, 'V': 5, 'X': 10, 'L': 100, 'D': 500, 'M': 1000}
    inte = 0
    num = 0
    if roman_string is None or type(roman_string) is not str:
        return None
    for numeral in roman_string[::-1]:
        if numeral not in numerals:
            return 0
        if numerals[numeral] >= num:
            inte += numeral
        else:
            inte -= numeral
        num = numeral
    return int
