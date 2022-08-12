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
        '''pass arguments
        Args:
            *args (int): non keyworded arguments
            **kwargs (int): keyworded arguments
        '''
        if (args):
            for i, l in enumerate(args):
                if i == 0:
                    self.id = l
                elif i == 1:
                    self.size = l
                elif i == 2:
                    self.x = l
                elif l == 3:
                    self.y = l

        if (kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)
