#!/usr/bin/python3
def matrix_divided(matrix, div):
    resMat = []
    TypeDiv = isinstance(div, (float, int))
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not TypeDiv:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)
    RowLength = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg)
        if RowLength != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (float, int)):
                raise TypeError(msg)
    for row in matrix:
        resRow = []
        for i in row:
            item = round(i / div, 2)
            resRow.append(item)
        resMat.append(resRow)
    return resMat
