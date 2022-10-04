#!/usr/bin/python3
""" Square class module - tested in tests/test_base.py """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square - inherits from Rectangle
        Attributes:
            size (int): The size of the new square
            x (int): The x coordinate of the new square
            y (int): The y coordinate of the new square
            id (int): the instantiation id of the new square
        Methods:
            __init__(self, size, x, y, id)
            __str__(self)
            size(self)
            size(self, value)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ init magic """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ string rep of square """
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.size)
