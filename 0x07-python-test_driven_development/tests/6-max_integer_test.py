#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        """Test max_integer function"""
        self.assertEqual(max_integer([12, 34, 5, 6, 15]), 34)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([-10, -5, -4, -2]), -2)
        self.assertEqual(max_integer([2.3, 1, -2, 1.8]), 2.3)
        self.assertEqual(max_integer([-4, 2, 10, 0, 2]), 10)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
