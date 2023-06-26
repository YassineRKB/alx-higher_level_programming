#!/usr/bin/python3
def magic_calculation(a, b):
    r = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            r = r + ((a ** b) / i)
        except Exception:
            r = a + b
            break
    return r
