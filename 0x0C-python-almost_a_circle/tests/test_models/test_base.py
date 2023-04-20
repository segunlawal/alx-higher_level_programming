#!/usr/bin/python3
"""
Unit test for the Base class
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def test_id_none(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id(self):
        b = Base(21)
        self.assertEqual(b.id, 21)

    def test_id_negative(self):
        b = Base(-21)
        self.assertEqual(b.id, -21)

    def test_id_string(self):
        b = Base("21")
        self.assertEqual(b.id, "21")

    def test_id_list(self):
        b = Base([1, 2, 6])
        self.assertEqual([1, 2, 6], b.id)
