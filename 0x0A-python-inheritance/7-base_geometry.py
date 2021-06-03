#!/usr/bin/python3
"""
Creates an class called BaseGeometry with a public instance
method for the area and integer validator
"""


class BaseGeometry:
    """ Class: BaseGeometry with area """
    def area(self):
        """ Area not yet implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates the input """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
