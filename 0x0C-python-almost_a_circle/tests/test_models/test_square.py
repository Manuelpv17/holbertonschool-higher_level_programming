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

    def test_square_update(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (4) 2/3 - 1")
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (12) 0/0 - 5")
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")
        s1.update(1, size=3, id=20, y=2)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")
