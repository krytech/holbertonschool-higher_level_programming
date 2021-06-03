#!/usr/bin/python3
"""
A rectangle class which inherits the class BaseGeometry
with a public instance method for the area and integer validator
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Initializes and validates with width and height """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
