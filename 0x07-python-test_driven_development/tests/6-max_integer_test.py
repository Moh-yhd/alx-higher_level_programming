#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Creates the TestMaxInteger class
    """
    def test_max(self):
        """Test the max_integer when given integer list
        """
        self.assertAlmostEqual(max_integer([1, 4, 6]), 6)
        self.assertAlmostEqual(max_integer([4, -6, 0]), 4)
        self.assertAlmostEqual(max_integer([4, 9, 0]), 9)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([7, 4.8, 7.2]), 7.2)

    def test_type(self):
        """Test if type errors are raised when neccessary
        """
        self.assertRaises(TypeError, max_integer, ["python", 1000, 1])
        self.assertRaises(TypeError, max_integer, [[4, 5], 8, 9])
        self.assertRaises(TypeError, max_integer, [(4, 8), 4, 9])
        self.assertRaises(TypeError, max_integer, [{'key': 'value'}, 4, 9])
