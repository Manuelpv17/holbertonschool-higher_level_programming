#!/usr/bin/python3
"""Search and update
    """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each
    line containing a specific string

        Keyword Arguments:
                filename {str} -- file (default: {""})
                search_string {str} -- text to search (default: {""})
                new_string {str} -- text to insert (default: {""})
        """
    with open(filename, mode="r+", encoding="utf-8") as m:
        new = ""
        cont = 0
        flag = 0
        for l in m.read():
            new += l
            if l == search_string[cont]:
                cont += 1
            else:
                cont == 0
            if cont == len(search_string):
                flag = 1
                cont = 0

            if l == '\n' and flag == 1:
                new += new_string
                flag = 0
        m.seek(0)
        m.write(new)
