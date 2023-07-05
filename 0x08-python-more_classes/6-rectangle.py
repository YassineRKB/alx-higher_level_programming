#!/usr/bin/python3
"""a class that defines a rectangle"""


class Rectangle:
    """class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    def __str__(self):
        msg = ""
        if self.width == 0 or self.height == 0:
            return msg
        else:
            for i in range(self.height):
                msg += "#" * self.width
                if i != self.height - 1:
                    msg += "\n"
            return msg

    def __repr__(self):
        msg = "Rectangle({}, {})".format(self.width, self.height)
        return msg

    def __del__(slef):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        TypeWid = isinstance(value, int)
        if not TypeWid:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        TypeHei = isinstance(value, int)
        if not TypeHei:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.height + self.width) * 2
