#!/usr/bin/python3
"""
Rectangle class that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """ Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter: width """
        return self.__width

    @property
    def height(self):
        """ Getter: height """
        return self.__height

    @property
    def x(self):
        """ Getter: x """
        return self.__x

    @property
    def y(self):
        """ Getter: y """
        return self.__y

    @width.setter
    def width(self, value):
        """ Setter: width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Setter: height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ Setter: x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ Setter: y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area value of the Rectangle instance """
        return self.__height * self.__width

    def display(self):
        """ Prints in stdout the Rectangle instance with char # """
        print("\n" * self.__y + "\n".join(" " * self.__x + "#" * self.__width
              for i in range(self.__height)))

    def __str__(self):
        """ Returns string representation of class """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.width, self.height)

    def update(self, *args, **kwargs):
        """ Updates class - assign an argument to each attribute """
        if args:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.width = v
                elif i == 2:
                    self.height = v
                elif i == 3:
                    self.x = v
                elif i == 4:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        dict = {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
        return dict
