#!/usr/bin/python3
"""module file for MyInt class"""


class MyInt(int):
    """MyInt rebel class"""
    def __eq__(self, other):
        return self.real != other

    def __ne__(self, other):
        return self.real == other
