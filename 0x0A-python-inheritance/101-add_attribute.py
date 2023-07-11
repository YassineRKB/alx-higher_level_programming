#!/usr/bin/python3
"""Module for add_attribute"""


def add_attribute(obj, att, value):
    """func to add attribute when possible"""
    typeAtt = hasattr(obj, "__doc__")
    attmsg = "can't add new attribute"
    if not typeAtt:
        raise TypeError(attmsg)
    setattr(obj, att, value)
