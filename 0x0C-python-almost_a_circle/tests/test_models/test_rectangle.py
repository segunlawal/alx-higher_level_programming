#!/usr/bin/python3
"""
Unit test for Rectangle class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        r1 = Rectangle(9, 2)
        self.assertEqual(r1.area(), 18)
        rect = Rectangle(3, 7, 8, 8, 2)
        self.assertEqual(rect.area(), 21)

    def setUp(self):
        Base.__Base__nb_objects = 0

    def test_rect(self):
        r0 = Rectangle(1, 2)
        self.assertEqual(r0.id, 3)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        self.assertEqual(r0.x, 0)
        self.assertEqual(r0.y, 0)
