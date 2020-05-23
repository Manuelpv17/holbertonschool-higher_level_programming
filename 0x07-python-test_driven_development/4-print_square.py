#!/usr/bin/python3
"""function that prints a square with the character #
    """


def print_square(size):
    """function that prints a square with the character #.

        Arguments:
                size {int} -- size length of the square

        Raises:
                TypeError: size must be an integer
                ValueError: size must be >= 0
        """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
