#!/usr/bin/python3
""" class file"""


class Square:
    """square class"""

    def __init__(self, size=0):
        sizetype = type(size)
        if sizetype is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        sqreArea = self._Square__size ** 2
        return sqreArea

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        sizetype = type(value)
        if sizetype is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value
