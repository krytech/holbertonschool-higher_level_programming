#!/usr/bin/python3
"""
A rectangle class with private attributes for
height and width, area and perimeter methods, prints
the rectangle using any given symbol, deletes itself and
keeps track of the number of instances for deletion
"""


class Rectangle:
    """ Rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes the rectangle """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """ Prints the rectangle using the symbol: # """
        if self.__height == 0 or self.__width == 0:
            return ""
        prt_it = "\n".join([str(self.print_symbol) * self.__width
                            for rows in range(self.__height)])
        return prt_it

    def __repr__(self):
        """ String representation to recreate a new instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Deletes instances of the rectangle class """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares two rectangles """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
