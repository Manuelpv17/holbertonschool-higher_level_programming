#!/usr/bin/python3
"""Read file
    """


def read_file(filename=""):
    """ reads a text file (UTF8) and
    prints it to stdou

        Keyword Arguments:
                filename {str} -- file with text (default: {""})
        """
    with open(filename, encoding="utf-8") as m:
        print(m.read(), end="")
