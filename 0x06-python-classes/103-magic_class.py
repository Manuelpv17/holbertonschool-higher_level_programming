#!/usr/bin/python3
"Task 10 ByteCode #5"
import math


class MagicClass:
    """Magic Radius class. Made from ByteCode"""

    def __init__(self, radius=0):
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self._MagicClass__radius = radius

    def area(self):
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        return 2 * math.pi * self._MagicClass__radius
