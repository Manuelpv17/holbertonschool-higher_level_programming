#!/usr/bin/python3
"""To JSON string
"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an
    object (string)

        Arguments:
                my_obj {unknow} -- object to be serialized

        Returns:
                str -- serialized string
        """
    return json.dumps(my_obj)
