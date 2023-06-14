#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixlen = len(matrix)
    neo = []
    for i in range(matrixlen):
        sqrootmap = lambda x: x ** 2, matrix[i]
        neo.append(list(map(sqrootmap)))
    return neo
