#!/usr/bin/python3
"""
Unittest for class Rectangle
Run all: python3 -m unittest discover tests
Run single: python3 -m unittest tests/test_models/test_rectangle.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class TestRectangle(unittest.TestCase):
    """ Tests for class Rectangle """

    def test_pep8(self):
        """ Pep8 test """
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, "Pep8 errors found")

    def test_attr_val(self):
        with self.assertRaises(TypeError):
            Rectangle("99", 1, 1, 1, 1)
            Rectangle([99, 98], 1, 1, 1, 1)
            Rectangle(1, {20, }, 1, 1, 1)
            Rectangle(1, {"s": 20}, 1, 1, 1)
            Rectangle(1, 1, None, 1, 1)
            Rectangle(1, 1, 1, (98, 99), 1)
        with self.assertRaises(ValueError):
            Rectangle(-99, 1, 1, 1, 1)
            Rectangle(1, -99, 1, 1, 1)
            Rectangle(1, 1, -99, 1, 1)
            Rectangle(1, 1, 1, -99, 1)

    def test_inval_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7, 8)

    def test_area(self):
        self.assertEqual(Rectangle(5, 5).area(), 25)

    def test_class(self):
        r = Rectangle(10, 10)
        self.assertEqual(type(r), Rectangle)
