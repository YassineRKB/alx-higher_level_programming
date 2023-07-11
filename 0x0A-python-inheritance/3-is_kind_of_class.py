#!/usr/bin/python3
"""module for is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """func to check if object is an instence of class, or
    of a class that it inhirets from"""
    return isinstance(obj, a_class)
