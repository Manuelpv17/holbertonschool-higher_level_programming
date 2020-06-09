#!/usr/bin/python3
"""tests!"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittest"""

    def test_square_now(self):
        self.assertEqual(Square(10, 2).id, 10)
        self.assertEqual(Square(10, 2, 0, 12).id, 12)
        self.assertEqual(Square(10, 2).id, 11)
        self.assertRaises(TypeError, Square)
        self.assertRaises(TypeError, Square, 1, 2, 3, 4, 5)

    def test_validate_attributes_square(self):
        self.assertRaises(ValueError, Square, -1, 2)
        self.assertRaises(ValueError, Square, 0, 2)
        self.assertRaises(ValueError, Square, 1, 3, -4)
        self.assertRaises(ValueError, Square, 1, -3, 4)
        self.assertRaises(TypeError, Square, "hi", 2)
        self.assertRaises(TypeError, Square, [], 2)
        self.assertRaises(TypeError, Square, (), 2)
        self.assertRaises(TypeError, Square, {}, 2)
        self.assertRaises(TypeError, Square, None, 2)
        self.assertRaises(TypeError, Square, 1, [], 4)
        self.assertRaises(TypeError, Square, 1, 3, [])
        self.assertRaises(TypeError, Square, 1, (), 4)
        self.assertRaises(TypeError, Square, 1, 3, ())
        self.assertRaises(TypeError, Square, 1, {}, 4)
        self.assertRaises(TypeError, Square, 1, 3, {})
        self.assertRaises(TypeError, Square, 1, None, 4)
        self.assertRaises(TypeError, Square, 1, 3, None)
        self.assertRaises(TypeError, Square, 1, "hi", 4)
        self.assertRaises(TypeError, Square, 1, 3, "hi")
