#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return None
    rnums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    previusNumeral = 0
    inte = 0
    for numeral in reversed(roman_string):
        if numeral.upper() not in rnums:
            return None
        numeral = rnums[numeral.upper()]
        if numeral >= previusNumeral:
            inte += numeral
        else:
            inte -= numeral
        previusNumeral = numeral
    return inte
