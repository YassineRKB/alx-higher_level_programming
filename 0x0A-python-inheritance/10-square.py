#!/usr/bin/python3
"""module for calss sqaure"""

rect = __import__('9-rectangle').Rectangle


class Square(rect):
    """Square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
