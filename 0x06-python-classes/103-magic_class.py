#!/usr/bin/python3
""" class file for MagicClass"""
from math import pi


class MagicClass:
    """magic class"""
    def __init__(self, rad=0):
        radType = type(rad)
        self._rad = 0
        if radType is not int and radType is not float:
            raise TypeError("radius must be an number")
        self._rad = rad
        return

    def area(self):
        areaR = pi * (self._rad ** 2)
        return areaR

    def circumference(self):
        circum = (pi * 2) * self._rad
        return circum
