#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        listlen = len(list) - 1
        nint = 0
        for integ in list:
            if nint != listlen:
                print("{:d}".format(integ), end=" ")
            else:
                print("{:d}".format(integ))
            nint += 1
    if matrix == [[]]:
        print("{}".format())
