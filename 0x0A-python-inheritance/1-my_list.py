#!/usr/bin/python3
"""Module for calss Mylist"""


class MyList(list):
    """Class Mylist that iherits from list"""
    
    def print_sorted(self):
        """func to print sorted list"""
        res = sorted(self)
        print(res)
