#!/usr/bin/python3
"""
Module to find a peak in a list of unsorted ints
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers using binary search.
    """
    length = len(list_of_integers)
    if length == 0:
        return None
    elif length == 1 or list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    elif list_of_integers[length - 1] >= list_of_integers[length - 2]:
        return list_of_integers[length - 1]
    left, right = 1, length - 2
    while left <= right:
        mid = (left + right) // 2
        if list_of_integers[mid] >= list_of_integers[mid - 1] and \
           list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1
