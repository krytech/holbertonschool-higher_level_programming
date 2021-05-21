#!/usr/bin/python3
"""
Unittest for 6-max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    A class to test the max integer function
    """
    def test_module_docstring(self):
        """ docstring test """
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)

    def test_function_docstring(self):
        """ docstring test """
        functionDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functionDoc) > 1)

    def test_ints_and_floats(self):
        """ tests for ints and floats """
        self.assertEqual(max_integer([25, 50, 100]), 100)
        self.assertEqual(max_integer([-25, -50, -100]), -25)
        self.assertEqual(max_integer([-25, 50, -100]), 50)
        self.assertEqual(max_integer([-1.5, -5.5]), -1.5)
        self.assertEqual(max_integer([10, -100, 10]), 10)
        self.assertEqual(max_integer([{2, 9}, {3}, {6}]), {2, 9})

    def test_string(self):
        """ tests for strings """
        self.assertEqual(max_integer("2579"), '9')
        self.assertEqual(max_integer("skgioz"), 'z')
        self.assertEqual(max_integer(["abc", 'm']), 'm')

    def test_list(self):
        """ testing the list """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([[1, 2], [2, 4]]), [2, 4])
