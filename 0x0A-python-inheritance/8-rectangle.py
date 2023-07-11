#!/usr/bin/python3
"""module for calss BaseGeometry"""


class BaseGeometry:
    """empty base class BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        msgType = "{} must be an integer".format(name)
        msgValue = "{} must be greater than 0".format(name)
        if type(value) is not int:
            raise TypeError(msgType)
        if value <= 0:
            raise ValueError(msgValue)
