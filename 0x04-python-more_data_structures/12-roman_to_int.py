#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    inte = 0
    num = 0
    if roman_string is None or type(roman_string) is not str:
        return None
    roman_string = roman_string.upper()
    for numeral in roman_string[::-1]:
        if numeral not in numerals:
            return None
        num = numerals[numeral]
        if numerals[numeral] <= num:
            inte += num
        else:
            inte -= num
        num = numeral
    return inte
