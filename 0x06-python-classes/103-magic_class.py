#!/usr/bin/python3
""" class file for MagicClass"""
import math


class MagicClass:
    """magic class"""
    def __init__(self, rad=0):
        radType = type(rad)
        self.__rad = 0
        if radType is not int and radType is not float:
            raise TypeError("radius must be an number")
        self.__rad = rad

    def area(self):
        return math.pi * self.__rad ** 2

    def circumference(self):
        return math.pi * 2 * self.__rad
