#!/usr/bin/python3
'''Defines square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''square class that inherits from rectangle.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''initialize data.
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.

        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''return square representation.'''
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        '''retrieve value'''
        return self.width

    @size.setter
    def size(self, value):
        '''set value of square width and height'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if (args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary representation of square"""
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["size"] = self.size
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict
