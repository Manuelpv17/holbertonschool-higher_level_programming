#!/usr/bin/python3
"""empty class Rectangle that defines a rectangle
    """


class Rectangle:
    """empty class Rectangle that defines a rectangle
        """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.width == 0:
            return 0
        return 2 * self.__height + 2 * self.width

    def __str__(self):
        r = ""
        if self.__height == 0 or self.width == 0:
            return r
        for h in range(self.height):
            for w in range(self.width):
                r += str(self.print_symbol)
            r += "\n"
        return r[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
