#!/usr/bin/python3
"""
Module to find a peak in a list of unsorted ints
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    """
    length = len(list_of_integers)

    if length == 0:
        return None

    if length == 1 or list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]

    if list_of_integers[length - 1] >= list_of_integers[length - 2]:
        return list_of_integers[length - 1]

    for i in range(1, length - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] \
                and list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]
