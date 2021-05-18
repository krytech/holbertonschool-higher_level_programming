#!/usr/bin/python3
"""A simple class definition for a Square"""


class Square:
    """Class Square definition"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

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

    @property
    def position(self):
        """Getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with
        the character # using x y position modifier"""
        square_size = self.__size
        if square_size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(square_size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(square_size):
                    print("#", end="")
                print()
