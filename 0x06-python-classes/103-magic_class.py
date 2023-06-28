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
        areaR = math.pi * (self.__rad ** 2)
        return areaR

    def circumference(self):
        circum = (math.pi * 2) * self.__rad
        return circum
