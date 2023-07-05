#!/usr/bin/python3
"""a class that defines a rectangle"""


class Rectangle:
    """class"""
    def __init__(self, width=0, heigth=0):
        self.width = width
        self.heigth = heigth

    @property
    def width(self):
        return self.__width

    @property
    def heigth(self):
        return self.__heigth

    @width.setter
    def width(self, value):
        TypeWid = isinstance(value, int)
        if not TypeWid:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @heigth.setter
    def heigth(self, value):
        TypeHei = isinstance(value, int)
        if not TypeHei:
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__heigth = value

