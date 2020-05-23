#!/usr/bin/python3
"""File for function add_integer
    """


def add_integer(a, b=98):
    """adds 2 integers

        Arguments:
                a {int or float} -- first number to be add
                b {int, float} -- second number to be add (default: {98})
        Raises:
                TypeError: a must be an integer
                TypeError: b must be an integer

        Returns:
                Int -- Addition of a and b
        """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
