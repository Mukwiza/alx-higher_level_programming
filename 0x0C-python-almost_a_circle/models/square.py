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
