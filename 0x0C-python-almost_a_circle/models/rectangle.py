#!/usr/bin/python3
'''Class Rectangle.'''
from models.base import Base


class Rectangle(Base):
    '''Defining rectangle class 
    inherits from :
        Base.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Assign each argument width, height, x and y to the right attribute.
        Args:
            width: width of rectangle.
            height: height of rectagle.
            x: number.
            y: number.
        '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''Returning private attribute.'''

        return self.__width

    @width.setter
    def width(self, value):
        '''setting private attribute.'''
        self.setter_validation('width', value)
        self.__width = value

    @property
    def height(self):
        '''Returning private attribute.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setting private attribute.'''
        self.setter_validation('height', value)
        self.__height = value

    @property
    def x(self):
        '''Returning private attribute.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setting private attribute.'''
        self.setter_validation('x', value)
        self.__x = value

    @property
    def y(self):
        '''Returning private attribute.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setting private attribute.'''
        self.setter_validation('y', value)
        self.__y = value

