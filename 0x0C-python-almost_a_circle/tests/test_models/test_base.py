#!/usr/bin/python3
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    def testBase(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 4)
