#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.height * self.width

    def display(self):
        for i in range(self.height + self.y):
            if i >= self.y:
                for j in range(self.width + self.x):
                    if j < self.x:
                        print(" ", end="")
                    else:
                        print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        data = ("id", "width", "height", "x", "y")
        for i, elem in enumerate(args):
            setattr(self, data[i], elem)

        if not args:
            for key, value in kwargs.items():
                if key in data:
                    setattr(self, key, value)

    def to_dictionary(self):
        d = {}
        data = ("id", "width", "height", "x", "y")
        for elm in data:
            d[elm] = getattr(self, elm)
        return d

    def to_csv(self):
        s = ""
        data = ("id", "width", "height", "x", "y")
        for elm in data:
            s += str(getattr(self, elm)) + ", "
        return s[:-2]
