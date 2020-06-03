#!/usr/bin/python3
"""Read n lines
    """


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8) and prints it to stdout

        Keyword Arguments:
                filename {str} -- file with text (default: {""})
                nb_lines {int} -- reads n lines of a text file (default: {0})
        """
    with open(filename, encoding="utf-8") as m:
        if nb_lines <= 0:
            print(m.read(), end="")
            return
        lines = m.readlines()
        if nb_lines > len(lines):
            nb_lines = len(lines)
        for i in range(nb_lines):
            print(lines[i], end="")
