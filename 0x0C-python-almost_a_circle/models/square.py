#!/usr/bin/python3
"""Model file for class square"""


Rectangle = __import__("base").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        super().valueChecker("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        lenarg = len(args)
        liargs = ["id", "size", "x", "y"]
        if args is not None and lenarg > 0:
            for i in range(lenarg):
                setattr(self, liargs[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])
