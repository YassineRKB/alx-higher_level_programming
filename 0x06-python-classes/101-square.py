#!/usr/bin/python3
""" class file"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        sizetype = type(size)
        posType = type(position)
        posElements = len(position)
        if sizetype is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
        if posType is not tuple or posElements != 2 \
                or type(position[0]) is not int \
                or type(position[1]) is not int \
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    def my_print(self):
        leg = self._Square__size
        lines = self.__position
        if leg == 0:
            print("")
        for a in range(lines[1]):
            print("")
        for b in range(leg):
            for i in range(lines[0]):
                print(" ", end="")
            for j in range(leg):
                print("#", end="")
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        posType = type(value)
        posElements = len(2)
        if posType is not tuple or posElements != 2 \
                or type(value[0]) is not int \
                or type(value[1]) is not int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        string = ""
        leg = self._Square__size
        lines = self.__position
        if leg == 0:
            return string
        for a in range(lines[1]):
            string += '\n'
        for b in range(leg):
            for j in range(lines[0]):
                string += " "
            for k in range(leg):
                string += "#"
            if b != leg - 1:
                string += '\n'
        return string
