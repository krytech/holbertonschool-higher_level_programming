#!/usr/bin/python3
"""
Unittest for class Base
Run all: python3 -m unittest discover tests
Run single: python3 -m unittest tests/test_models/test_base.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class TestBase(unittest.TestCase):
    """ Tests for class base """

    def test_id(self):
        """ Test for id """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_pep8(self):
        """ Pep8 test """
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/base.py", "tests/test_models/test_base.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, "Pep8 errors found")

    def test_inval_args(self):
        with self.assertRaises(TypeError):
            Base(199, 255)
