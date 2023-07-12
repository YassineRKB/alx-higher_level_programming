#!/usr/bin/python3
"""Module pascal's triangle"""


def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        res = [1] * (i + 1)
        triangle.append(res)
        trilen = len(triangle[i])
        for k in range(trilen):
            try:
                if i < 1 or k < 1:
                    raise IndexError
                triangle[i][k] = triangle[i - 1][k] + triangle[i - 1][k - 1]
            except IndexError:
                pass
    return triangle
