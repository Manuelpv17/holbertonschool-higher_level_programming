#!/usr/bin/python3
"""Save Object to a file
    """
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

        Arguments:
                my_obj {unknow} -- object to be save as string
                filename {str} -- name of file
        """
    with open(filename, mode="w", encoding="utf-8") as m:
        json.dump(my_obj, m)
