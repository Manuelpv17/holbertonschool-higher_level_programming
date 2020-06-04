#!/usr/bin/python3
"""Class to JSON
    """


def class_to_json(obj):
    """returns the dictionary description
    with simple data structure (list,
    dictionary, string, integer and boolean)
    for JSON serialization of an object

        Arguments:
                obj {unknow} -- object

        Returns:
                dictionary -- list of attributes
        """
    return obj.__dict__
