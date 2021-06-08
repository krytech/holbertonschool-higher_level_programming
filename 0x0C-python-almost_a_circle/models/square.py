#!/usr/bin/python3
"""
Square class that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ Getter: size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter: size """
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns string representation of class """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    def update(self, *args, **kwargs):
        """ Updates class - assign an argument to each attribute """
        if args:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.size = v
                elif i == 2:
                    self.x = v
                elif i == 3:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        dict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return dict
