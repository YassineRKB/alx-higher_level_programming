#!/usr/bin/python3
"""class locked"""


class LockedClass:
    """
    class LockedClass
    Prevents any instances unless its first_name
    """
    __slots__ = ["first_name"]
