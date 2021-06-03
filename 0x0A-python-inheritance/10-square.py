#!/usr/bin/python3
"""
A suqare class which inherits properties from the subclass
rectangle and the parent class BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ New square class that inherits properties from Rectangle """
    def __init__(self, size):
        """ initializes size """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
