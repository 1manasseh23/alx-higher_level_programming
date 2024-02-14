#!/usr/bin/python3

from models.rectangle import Rectangle
import unittest
import warnings
"""
Testrectangle its a function that test the
unittest for Rectangle class
"""


class Testrectangle(unittest.TestCase):
    """
    This test checks if the two values passed as arguments
    are equal. If they are not, the test fails
    """
    def test_equal(self):
        self.assertEqual(1, 1)
    """
    This test checks if the two values passed as arguments
    are not equal. If they are, the test fails
    """
    def test_not_equal(self):
        self.assertNotEqual(1, 2)
    """
    his test checks if the value passed as an
    argument is true. If it is not, the test fails
    """
    def test_true(self):
        self.assertTrue(True)
    """
    This test checks if the value passed as an
    argument is false. If it is not, the test fails
    """
    def test_false(self):
        self.assertFalse(False)
    """
    This test checks if two objects are the same
    object. If they are not, the test fails
    """
    def test_is(self):
        a = Rectangle(10, 20)
        b = Rectangle(10, 20)
        self.assertIs(a, b)
    """
    This test checks if two objects are not the
    same object. If they are, the test fails
    """
    def test_is_not(self):
        a = Rectangle()
        b = Rectangle()
        self.assertIsNot(a, b)
    """
    This test checks if an object is None.
    If it is not, the test fails.
    """
    def test_is_none(self):
        a = Rectangle()
        self.assertIsNone(a.id)
    """
    This test checks if an object is not None.
    If it is, the test fails
    """
    def test_is_not_none(self):
        a = Rectangle()
        self.assertIsNotNone(a)
    """
    This test checks if an item is in a
    container. If it is not, the test fails
    """
    def test_in(self):
        a = Rectangle()
        b = Rectangle(1)
        self.assertIn(b, a)
    """
    This test checks if an item is not
    in a container. If it is, the test fails
    """
    def test_not_in(self):
        a = Rectangle()
        b = Rectangle(4)
        self.assertNotIn(b, a)
    """
    This test checks if an object is an instance of
    a given class. If it is not, the test fails
    """
    def test_is_instance(self):
        a = Rectangle()
        self.assertIsInstance(a, Rectangle)
    """
    This test checks if an object is not an instance
    of a given class. If it is, the test fails
    """
    def test_not_is_instance(self):
        a = Rectangle()
        self.assertNotIsInstance(a, str)
    """
    This test checks if a function raises a specific
    exception. If it does not, the test fails
    Return:
        1 / 0
    """
    def test_raises(self):
        def divide_by_zero():
            return 1 / 0

        self.assertRaises(ZeroDivisionError, divide_by_zero)

    """
    This test checks if a function raises a specific exception
    with a specific error message. If it does not, the test fails
    """
    def test_raises_regex(self):
        def raise_value_error():
            raise ValueError("Invalid value")

        self.assertRaisesRegex(ValueError, "Invalid value", raise_value_error)

    """
    This test checks if a function raises a warning. If it
    does not, the test fails
    """
    def test_warns(self):
        def warn():
            warnings.warn("This is a warning message")

        self.assertWarns(Warning, warn)

    """
    This function tests if two floating-point numbers are
    approximately equal
    """
    def test_almost_equal(self):
        a = 1.0
        b = 1.0000001
        self.assertAlmostEqual(a, b)


if __name__ == '__main__':
    unittest.main()
