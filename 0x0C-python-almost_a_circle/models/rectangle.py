#!/usr/bin/python3
"""Model file for class rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor for rectangle class"""
        self.valueChecker("width", width)
        self.valueChecker("height", height)
        self.valueChecker("x", x)
        self.valueChecker("y", y)
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter: width"""
        return self.__width

    @property
    def height(self):
        """getter: height"""
        return self.__height

    @property
    def x(self):
        """getter: x"""
        return self.__x

    @property
    def y(self):
        """getter: y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter: width"""
        self.valueChecker("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """setter: height"""
        self.valueChecker("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """setter: x"""
        self.valueChecker("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """setter: y"""
        self.valueChecker("y", value)
        self.__y = value

    def valueChecker(self, var, val):
        """method: value checker"""
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
        """method: area"""
        resarea = self.width * self.height
        return resarea

    def display(self):
        """method: display"""
        resoutput = "\n" * self.y
        for i in range(self.height):
            resoutput += " " * self.x
            for j in range(self.width):
                resoutput += "#"
            resoutput += "\n"
        print(resoutput, end="")

    def __str__(self):
        """method: str"""
        resstr = f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} \
            - {self.width}/{self.height}"
        return resstr

    def update(self, *args, **kwargs):
        """method: update"""
        lenarg = len(args)
        liargs = ["id", "width", "height", "x", "y"]
        if args is not None and lenarg > 0:
            for i in range(lenarg):
                setattr(self, liargs[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])
