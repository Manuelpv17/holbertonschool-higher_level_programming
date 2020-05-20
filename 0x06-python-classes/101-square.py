#!/usr/bin/python3
"""File for defining Class Square"""


class Square:
    """class Square that defines a square """

    def __init__(self, size=0, position=(0, 0)):
        self.check_size(size)
        self.check_position(position)
        self.__size = size
        self.__position = position

    def check_size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def check_position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or type(value[1]) is not int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        if self.__size == 0:
            print()
            return
        for j in range(self.__size + self.position[1]):
            if j < self.position[1]:
                print()
            else:
                for i in range(self.__size + self.position[0]):
                    if i < self.position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.check_position(value)
        self.__position = value

    def __str__(self):
        if self.__size == 0:
            return
        for j in range(self.__size + self.position[1]):
            if j < self.position[1]:
                print()
            else:
                for i in range(self.__size + self.position[0]):
                    if i < self.position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                if j != self.__size + self.position[1] - 1:
                    print()
        return ""
