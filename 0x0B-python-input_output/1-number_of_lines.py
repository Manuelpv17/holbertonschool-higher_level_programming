#!/usr/bin/python3
"""Number of lines
    """


def number_of_lines(filename=""):
    """number of lines of a text file

        Keyword Arguments:
                filename {str} -- file with text (default: {""})

        Returns:
                int -- number of lines of a text file
        """
    with open(filename) as m:
        return len(m.readlines())
