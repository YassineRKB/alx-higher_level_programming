#!/usr/bin/python3
"""module for calss BaseGeometry"""

BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """empty base class BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
