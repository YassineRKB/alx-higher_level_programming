#!/usr/bin/python3
"""Model file for class square"""


Rectangle = __import__("base").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

