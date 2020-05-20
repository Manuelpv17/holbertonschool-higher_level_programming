#!/usr/bin/python3
"""File for defining Class Square"""


class Square:
    """class Square that defines a square """

    def __init__(self, size=0):
        self.check_size(size)
        self.__size = size

    def check_size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.check_size(value)
        self.__size = value

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
