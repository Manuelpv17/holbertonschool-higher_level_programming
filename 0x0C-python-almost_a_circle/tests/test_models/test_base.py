#!/usr/bin/python3
"""tests!"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittest"""

    def test_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        b = pep8style.check_files(['models/base.py'])
        self.assertEqual(
            b.total_errors, 0, "Found code style errors (and warnings).")
        r = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(
            r.total_errors, 0, "Found code style errors (and warnings).")
        s = pep8style.check_files(['models/square.py'])
        self.assertEqual(
            s.total_errors, 0, "Found code style errors (and warnings).")
