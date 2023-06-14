#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    matrixlen = len(matrix)
    neo = []
    for i in range(matrixlen):
        neo.append(list(map(lambda x: x ** 2, matrix[i])))
    return neo
