#!/usr/bin/python3
"""empty class Rectangle that defines a rectangle
    """


class Rectangle:
    """empty class Rectangle that defines a rectangle
        """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.check_height(value)
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.check_width(value)
        self.__width = value

    def check_width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    def check_height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
