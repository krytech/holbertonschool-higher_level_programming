#!/usr/bin/python3
"""
Unittest for class Square
Run all: python3 -m unittest discover tests
Run single: python3 -m unittest tests/test_models/test_square.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class TestSquare(unittest.TestCase):
    """ Tests for class Rectangle """

    def test_pep8(self):
        """ Pep8 test """
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/square.py", "tests/test_models/test_square.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, "Pep8 errors found")

    def test_area(self):
        self.assertEqual(Square(5).area(), 25)

    def test_inval_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7, 8)

    def test_attr_val(self):
        """Test attributes are validated before set"""
        with self.assertRaises(TypeError):
            Square("50")
            Square([50, 5])
            Square({20, })
            Square({"s": 20})
            Square(None)
            Square((40, 50), 4)
        with self.assertRaises(ValueError):
            Square(-5)
            Square(91).size(-19)

    def test_class(self):
        s = Square(10)
        self.assertEqual(type(s), Square)
