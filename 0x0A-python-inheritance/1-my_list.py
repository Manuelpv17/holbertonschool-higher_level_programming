#!/usr/bin/python3
"""Task Mylist
    """


class MyList(list):
    """class MyList that inherits from list
        """

    def print_sorted(self):
        new = self.copy()
        new.sort()
        print(new)
