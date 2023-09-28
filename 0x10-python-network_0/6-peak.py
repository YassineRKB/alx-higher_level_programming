#!/usr/bin/python3
"""
Module to find a peak in a list of unsorted ints
"""


def find_peak(list_of_integers, left=None, right=None):
    """
    Find a peak in a list of unsorted integers using binary search.
    """
    if not list_of_integers:
        return None
    if left is None:
        left = 0
    if right is None:
        right = len(list_of_integers) - 1
    mid = (left + right) // 2
    if list_of_integers[mid] < list_of_integers[mid + 1]:
        left = mid + 1
    else:
        right = mid
    if left == right:
        return list_of_integers[left]
    return find_peak(list_of_integers, left, right)
