#!/usr/bin/python3
"""Write to a file
    """


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written

        Keyword Arguments:
                filename {str} -- name of file (default: {""})
                text {str} -- text to be written (default: {""})

        Returns:
                int -- number of characters
        """
    with open(filename, mode="w", encoding="utf-8") as m:
        return m.write(text)
