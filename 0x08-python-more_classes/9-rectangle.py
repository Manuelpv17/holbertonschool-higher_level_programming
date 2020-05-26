#!/usr/bin/python3


"""class Rectangle that defines a rectangle and define
the methods getter and setter for the attributes width and height
Adding method __str__ to print the rectangle
"""


class Rectangle:
    """Define a Rectangle.
    Attributes:
        width: private instance attribute
        height: private instance attribute
        number_of_instances: Class variables also known
        as static variables are declared with the static keyword
        in a class, but outside a method, constructor or a block.
        print_symbol: Public class attribute Initialized to #
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of the instance attributes
            Args:
            width(int): private, zero or positive number
            height(int): private, zero or positive number
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """method which is used for getting
            a value is decorated with "@property"
            (also known as 'accessor')
            These methods are of course the getter for retrieving the data
            and the setter for changing the data. According to this principle,
            the attributes of a class are made private to hide and protect them
            from other code.
            Return: the data value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """method which has to function as the setter is to change
            the value and is decorated with "@methodname.setter"
            (also know as 'mutator')
            These methods are of course the getter for retrieving the data
            and the setter for changing the data. According to this principle,
            the attributes of a class are made private to hide and protect them
            from other code.
            Changes the data
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """method which is used for getting
            a value is decorated with "@property"
            (also known as 'accessor')
            These methods are of course the getter for retrieving the data
            and the setter for changing the data. According to this principle,
            the attributes of a class are made private to hide and protect them
            from other code.
            Return: the data value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """method which has to function as the setter is to change
            the value and is decorated with "@methodname.setter"
            (also know as 'mutator')
            These methods are of course the getter for retrieving the data
            and the setter for changing the data. According to this principle,
            the attributes of a class are made private to hide and protect them
            from other code.
            Changes the data
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle
            Return: the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a rectangle
            Return: the rectangle perimiter
        """
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Method to print a attribute "informal"
        """
        string = ""
        if (self.__width == 0) or (self.__height == 0):
            return string
        if not isinstance(self.print_symbol, str):
            self.print_symbol = str(self.print_symbol)
        for i in range(self.__height - 1):
            string += (self.print_symbol * self.__width) + "\n"
        string += (self.print_symbol * self.__width)
        return string

    def __repr__(self):
        """Method to return the representation of the object
           "formal" printing
            repr() should return a string representation
            of the rectangle to be able to recreate a new instance
            by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """The method __del__ is the instance method called when
            an instance is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method to compare the area of two rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.__width * rect_1.__height
        area2 = rect_2.__width * rect_2.__height
        if area1 > area2:
            return rect_1
        elif area1 < area2:
            return rect_2
        elif area1 == area2:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Class method to create a square
           cls refers to the init method and the magic
           so it will create a the same class type when using cls
        """
        return cls(size, size)
