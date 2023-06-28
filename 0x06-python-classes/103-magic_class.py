#!/usr/bin/python3
""" class file for MagicClass"""
import math


class MagicClass:
    """magic class"""
    def __init__(self, rad=0):
        radType = type(rad)
        if radType is not int:
            raise TypeError("radius must be an number")
        self._rad = rad

    def area(self):
        pass

    def circumference(self):
        pass
