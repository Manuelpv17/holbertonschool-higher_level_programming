#!/usr/bin/python3
"""function that adds a new attribute to an
object if it’s possible
    """


def add_attribute(obj, att, value):
    """adds a new attribute
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, att, value)
