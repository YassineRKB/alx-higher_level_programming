#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixlen = len(matrix)
    neo = []
    for i in range(matrixlen):
        sqrootmap = lambda x: x ** 2
        neo.append(list(map(sqrootmap, matrix[i])))
    return neo
