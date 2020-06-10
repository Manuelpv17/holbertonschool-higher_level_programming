#!/usr/bin/python3
"""tests!"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittest"""

    def test_first_rectangle(self):
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)
        self.assertEqual(Rectangle(10, 2).id, 2)
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
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (2) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (2) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (2) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        r1.update(89, 2, 3, 4, 5, x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        r1.update(90, x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (90) 4/5 - 2/3")

    def test_to_dict(self):
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.to_dictionary(),
                         {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        self.assertEqual(str(type(r1.to_dictionary())),
                         "<class 'dict'>")
        self.assertEqual(str(type(r1.to_dictionary())),
                         "<class 'dict'>")
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/9 - 10/2")
        self.assertEqual(r1 == r2, False)

    def tearDown(self):
        """Tears down obj count
        """
        Base._Base__nb_objects = 0

    def test_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")
