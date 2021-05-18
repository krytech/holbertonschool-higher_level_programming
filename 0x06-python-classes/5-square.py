#!/usr/bin/python3
"""A simple class definition for a Square"""


class Square:
    """Class Square definition"""
    def __init__(self, size=0):
        """Initializes Square"""
        self.__size = size

    def area(self):
        """Calculates area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        square_size = self.__size
        if square_size == 0:
            print()
        for i in range(square_size):
            for j in range(square_size):
                print("#", end="")
            print()
