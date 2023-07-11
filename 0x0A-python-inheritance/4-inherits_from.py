#!/usr/bin/python3
"""module for inherits_from"""


def inherits_from(obj, a_class):
    """func to check if obj in an instence of a class that inherits
    from the specific class"""

    subClass = issubclass(type(obj), a_class)
    typeClass = type(obj) != a_class
    return subClass and typeClass
