#!/usr/bin/python3
from sys import argv


def check(i, j, Board):
    for item in Board:
        absItem0 = abs(i - item[0])
        absItem1 = abs(j - item[1])
        if (i == item[0] or j == item[1] or absItem0 == absItem1):
            return False
    return True

def backTrack(n, position, qboard, sboard):
    if position == n:
        sboard.append(qboard.copy())
        return

    for column in range(n):
        if check(position, column, qboard):
            qboard.append([position, column])
            backTrack(n, position + 1, qboard, sboard)
            qboard.pop()

if __name__ == "__main__":
    arglen = len(argv)
    if arglen != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
    solutions = []
    queens = []
    backTrack(n, 0, queens, solutions)
    for solution in solutions:
        print(solution)
