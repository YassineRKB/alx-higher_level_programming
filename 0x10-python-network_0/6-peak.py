#!/usr/bin/python3
"""
Module to find a peak in a list of unsorted ints
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers using binary search.
    """
    for idx, num in enumerate(list_of_integers):
        prev = list_of_integers[idx - 1] if idx > 0 \
            else float('-inf')
        next = list_of_integers[idx + 1] if idx < len(list_of_integers) - 1 \
            else float('-inf')
        if num >= prev and num >= next:
            return num
