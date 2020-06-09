#!/usr/bin/python3
""" Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area function"""
        return self.height * self.width

    def display(self):
        """draw of #"""
        for i in range(self.height + self.y):
            if i >= self.y:
                for j in range(self.width + self.x):
                    if j < self.x:
                        print(" ", end="")
                    else:
                        print("#", end="")
            print()

    def __str__(self):
        """representation string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update function"""
        data = ("id", "width", "height", "x", "y")
        for i, elem in enumerate(args):
            setattr(self, data[i], elem)

        if not args:
            for key, value in kwargs.items():
                if key in data:
                    setattr(self, key, value)

    def to_dictionary(self):
        """from object to dictionary"""
        d = {}
        data = ("id", "width", "height", "x", "y")
        for elm in data:
            d[elm] = getattr(self, elm)
        return d

    def to_csv(self):
        """from object to csv format"""
        s = ""
        data = ("id", "width", "height", "x", "y")
        for elm in data:
            s += str(getattr(self, elm)) + ", "
        return s[:-2]
