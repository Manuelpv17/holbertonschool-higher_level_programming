#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])
"""

    def test_condition(self):
        """Test None if empty list
                """
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))

    def test_type_error(self):
        """test type error
                """
        self.assertRaises(TypeError, max_integer, 42)
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, 100000000)
        self.assertRaises(TypeError, max_integer, -100000000)

    def test_options(self):
        """Test different inputs
                """
        self.assertEqual(max_integer([5, 2, 3]), 5)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-1.1, 0.2, 0.22]), 0.22)
        self.assertEqual(max_integer("Hello"), "o")
        self.assertEqual(max_integer("Hello"), "o")
