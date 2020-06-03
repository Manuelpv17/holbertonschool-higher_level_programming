#!/usr/bin/python3
"""My integer
    """


class MyInt(int):

    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        return self.num != other

    def __ne__(self, other):
        return self.num == other
