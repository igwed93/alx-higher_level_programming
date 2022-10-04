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
            update(self, *args, **kwargs)
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

    def update(self, *args, **kwargs):
        """ update instance attributes via */**args
            *args:
                .. 1st argument represents id attribute
                .. 2nd argument represents size attribute
                .. 3rd argument represents x attribute
                .. 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            n = 0
            for arg in args:
                if n == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif n == 1:
                    self.size = arg
                elif n == 2:
                    self.x = arg
                elif n == 3:
                    self.y = arg
                n += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """dictionary rep of square"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):
        """ string rep of square """
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.size)


if __name__ == "__main__":
    Square()
