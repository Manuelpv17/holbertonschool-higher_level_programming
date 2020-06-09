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
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 1)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5, 6)

    def test_validate_attributes(self):
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3, 4)
        self.assertRaises(TypeError, Rectangle, "hi", 2)
        self.assertRaises(TypeError, Rectangle, 1, "hi")
        self.assertRaises(TypeError, Rectangle, [], 2)
        self.assertRaises(TypeError, Rectangle, 1, [])
        self.assertRaises(TypeError, Rectangle, (), 2)
        self.assertRaises(TypeError, Rectangle, 1, ())
        self.assertRaises(TypeError, Rectangle, {}, 2)
        self.assertRaises(TypeError, Rectangle, 1, {})
        self.assertRaises(TypeError, Rectangle, None, 2)
        self.assertRaises(TypeError, Rectangle, 1, None)
        self.assertRaises(TypeError, Rectangle, 1, 2, [], 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, [])
        self.assertRaises(TypeError, Rectangle, 1, 2, (), 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, ())
        self.assertRaises(TypeError, Rectangle, 1, 2, {}, 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, {})
        self.assertRaises(TypeError, Rectangle, 1, 2, None, 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, None)
        self.assertRaises(TypeError, Rectangle, 1, 2, "hi", 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "hi")
