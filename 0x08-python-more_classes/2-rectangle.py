#!/usr/bin/python3
"""
A rectangle class with private attributes for
height and width, and area and perimeter methods
"""


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ Initializes the rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter that returns the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width for an int > 0 """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter that returns the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height for an int > 0 """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of the rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
