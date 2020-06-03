#!/usr/bin/python3
"""Task Mylist
    """


class MyList(list):
    """class MyList that inherits from list
        """

    def print_sorted(self):
        """print sorted
                """
        new = self.copy()
        new.sort()
        print(new)
