#!/usr/bin/python3
"""From JSON string to Object
"""
import json


def from_json_string(my_str):
    """returns an object
    (Python data structure)
    represented by a JSON string

        Arguments:
                my_str {str} -- string to be decode

        Returns:
                pyhon object -- decode json
        """
    return json.loads(my_str)
