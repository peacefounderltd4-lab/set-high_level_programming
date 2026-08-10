#!/usr/bin/python3
"""Unittest for max_integer."""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer."""

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative(self):
        self.assertEqual(max_integer([-4, -2, -8, -1]), -1)

    def test_all_negative(self):
        self.assertEqual(max_integer([-10, -20, -30]), -10)

    def test_same_values(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_max_first(self):
        self.assertEqual(max_integer([10, 3, 2, 1]), 10)

    def test_max_last(self):
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_float_values(self):
        self.assertEqual(max_integer([1.5, 4.5, 2.2]), 4.5)


if __name__ == '__main__':
    unittest.main()
