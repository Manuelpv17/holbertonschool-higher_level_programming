#!/usr/bin/python3
"""Append to a file
    """


def append_write(filename="", text=""):
    """Write a function that appends a string
    at the end of a text file (UTF8) and returns the number of characters added

        Keyword Arguments:
                filename {str} -- name of file (default: {""})
                text {str} -- text to be written (default: {""})

        Returns:
                int -- number of characters
        """
    with open(filename, mode="a", encoding="utf-8") as m:
        return m.write(text)
