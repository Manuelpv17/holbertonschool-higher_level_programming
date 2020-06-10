#!/usr/bin/python3
"""tests!"""
import unittest
import pep8
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
        self.assertCountEqual(
            json_dictionary, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
        self.assertEqual(type(json_dictionary), str)

    def test_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")
