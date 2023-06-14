#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    matrixlen = len(matrix)
    antat = []
    for i in range(matrixlen):
        antat.append(list(map(lambda x: x ** 2, matrix[i])))
    return antat
