#!/usr/bin/python3
"""
test_square module
"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        Base.__Base__nb_objects = 0

    def test_square(self):
        s0 = Square(1)
        self.assertEqual(s0.id, 4)
        self.assertEqual(s0.width, 1)
        self.assertEqual(s0.height, 1)
        self.assertEqual(s0.x, 0)
        self.assertEqual(s0.y, 0)
        self.assertEqual(s0.area(), 1)
