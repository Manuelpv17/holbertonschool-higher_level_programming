#!/usr/bin/python3
"""tests!"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittest"""

    def test_first_rectangle(self):
        self.assertEqual(Rectangle(10, 2).id, 5)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)
        self.assertEqual(Rectangle(10, 2).id, 6)
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

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        pass

    def test_str(self):
        self.assertEqual(Rectangle(4, 6, 2, 1, 12).__str__(),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(Rectangle(5, 5, 1).__str__(),
                         "[Rectangle] (7) 1/0 - 5/5")
