#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """Module for calss Mylist"""

    def print_sorted(self):
        """func to print sorted list"""
        print(sorted(self))
