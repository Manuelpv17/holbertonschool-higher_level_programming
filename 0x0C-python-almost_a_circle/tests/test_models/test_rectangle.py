#!/usr/bin/python3
"""tests!"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittest"""

    def test_first_rectangle(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 3)
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)
        r2 = Rectangle(10, 2)
        self.assertEqual(r2.id, 4)
