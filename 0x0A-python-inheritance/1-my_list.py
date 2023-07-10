#!/usr/bin/python3
"""Module 1-my_list, class MyList that inherits list"""


class MyList(list):
    """calss Mylist inherits List"""

    def print_sorted(self):
        """func to print sorted list in ascending order"""
        print(sorted(self))
