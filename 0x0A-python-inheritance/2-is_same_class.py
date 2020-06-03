#!/usr/bin/python3
"""Exact same object
    """


def is_same_class(obj, a_class):
    """CHeck exact same object

        Arguments:
                obj {[type]} -- Object
                a_class {[type]} -- Class

        Returns:
                Boolean -- True if exact same
        """
    return type(obj) is a_class
