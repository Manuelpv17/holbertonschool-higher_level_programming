#!/usr/bin/python3
"""tests!"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittest"""

    def test_base_class(self):
        """Test base"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 2)
        self.assertRaises(TypeError, Base, 1, 2)

    def tearDown(self):
        """Tears down obj count
        """
        Base._Base__nb_objects = 0

    def test_dict_to_json(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(
            dictionary, {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(json_dictionary, "[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]")
        self.assertEqual(type(json_dictionary), str)
