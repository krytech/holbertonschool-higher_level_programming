#!/usr/bin/python3
"""A simple class definition for a Square"""


class Square:
    """Class Square definition"""
    def __init__(self, size=0):
        """Initializes Square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates area of the square"""
        return self.__size ** 2
