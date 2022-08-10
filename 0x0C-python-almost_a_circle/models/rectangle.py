#!/usr/bin/python3
'''Class Rectangle.'''
from models.base import Base


class Rectangle(Base):
    '''Defining rectangle class inherits from base.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''returning private attribute.'''

        return self.__width

    @width.setter
    def width(self, value):
        '''setting private attribute.'''
        self.setter_validation('width', value)
        self.__width = value

    @property
    def height(self):
        '''returning private attribute.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setting private attribute.'''
        self.setter_validation('height', value)
        self.__height = value

    @property
    def x(self):
        '''returning private attribute.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setting private attribute.'''
        self.setter_validation('x', value)
        self.__x = value

    @property
    def y(self):
        '''returning private attribute.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setting private attribute.'''
        self.setter_validation('y', value)
        self.__y = value

