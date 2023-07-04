#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    TypeFirst = isinstance(first_name, str)
    TypeLast = isinstance(last_name, str)
    if not TypeFirst:
        raise TypeError("first_name must be a string")
    if not TypeLast:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
