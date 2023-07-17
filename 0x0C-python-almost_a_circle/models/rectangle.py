#!/usr/bin/python3
"""Model file for class rectangle"""


Base = __import__("base").Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.valueChecker("width", width)
        self.valueChecker("height", height)
        self.valueChecker("x", x)
        self.valueChecker("y", y)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.valueChecker("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.valueChecker("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.valueChecker("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.valueChecker("y", value)
        self.__y = value

    def valueChecker(self, var, val):
        typeInt = isinstance(val, int)
        MsgMustBeInt = " must be integer"
        MsgMustBePos = " must be > 0"
        MsgMustbePosOrZero = " must be >= 0"
        if val is not None and not typeInt:
            raise TypeError(var + MsgMustBeInt)
        if val <= 0 and (var == "height" or var == "width"):
            raise ValueError(var + MsgMustBePos)
        if val < 0 and (var == "x" or var == "y"):
            raise ValueError(var + MsgMustbePosOrZero)

    def area(self):
        resarea = self.width * self.height
        return resarea

    def display(self):
        resoutput = "\n" * self.y
        for i in range(self.height):
            resoutput += " " * self.x
            for j in range(self.width):
                resoutput += "#"
            resoutput += "\n"
        print(resoutput, end="")

    def __str__(self):
        resstr = f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} \
            - {self.width}/{self.height}"
        return resstr
