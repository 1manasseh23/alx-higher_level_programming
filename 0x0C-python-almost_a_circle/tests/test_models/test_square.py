#!/usr/bin/python3

from models.square import Square
import unittest
import warnings

class Testsquare(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(1, 1)

    def test_not_equal(self):
        self.assertNotEqual(1, 2)

    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)

    def test_is(self):
        a = Square()
        b = a
        self.assertIs(a, b)

    def test_is_not(self):
        a = Square()
        b = Square()
        self.assertIsNot(a, b)

    def test_is_none(self):
        a = Square()
        self.assertIsNone(a.id)

    def test_is_not_none(self):
        a = Square()
        self.assertIsNotNone(a)

    def test_in(self):
        a = Square()
        b = Square(1)
        self.assertIn(b, a)

    def test_not_in(self):
        a = Square()
        b = Square(4)
        self.assertNotIn(b, a)

    def test_is_instance(self):
        a = Square()
        self.assertIsInstance(a, Rectangle)

    def test_not_is_instance(self):
        a = Square()
        self.assertNotIsInstance(a, str)

    def test_raises(self):
        def divide_by_zero():
            return 1 / 0

        self.assertRaises(ZeroDivisionError, divide_by_zero)

    def test_raises_regex(self):
        def raise_value_error():
            raise ValueError("Invalid value")

        self.assertRaisesRegex(ValueError, "Invalid value", raise_value_error)

    def test_warns(self):
        def warn():
            warnings.warn("This is a warning message")

        self.assertWarns(Warning, warn)
"""
    def test_almost_equal(self):
        a = 1.0
        b = 1.0000001
        self.assertAlmostEqual(a, b)
"""
if __name__ == '__main__':
    unittest.main()
