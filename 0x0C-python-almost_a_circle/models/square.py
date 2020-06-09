#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update function"""
        data = ("id", "size", "x", "y")
        for i, elem in enumerate(args):
            setattr(self, data[i], elem)

        if not args:
            for key, value in kwargs.items():
                if key in data:
                    setattr(self, key, value)

    def to_dictionary(self):
        """from object to dictionary"""
        d = {}
        data = ("id", "size", "x", "y")
        for elm in data:
            d[elm] = getattr(self, elm)
        return d

    def to_csv(self):
        """from objecto to csv format"""
        s = ""
        data = ("id", "size", "x", "y")
        for elm in data:
            s += str(getattr(self, elm)) + ", "
        return s[:-2]
