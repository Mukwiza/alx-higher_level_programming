#!/usr/bin/python3
"""First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """rectangle class that inherits from.
    the base class
    Args:
        Base(model): the inherited model
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructs the rectange's attributes.
        Args:
            height(int): rectangle's height
            width(int): rectangle's width
            x(int): input value
            y(int): input value
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """gets the Width of the rectangle.
        Returns:
            width (int): value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the Width (private) of the rectangle
        Args:
            value(int): value of the rectangle
        """
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """gets the height (private) of the rectangle
        Returns:
            height (int): value fo height
        """
        return self.__height

    @width.setter
    def height(self, value):
        """sets the height(private) of the rectangle
          Args:
            value(int): value of the rectangle
        """
        if type(value) not in [int]:
            raise TypeError("height must be an integer")

       if value <= 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def x(self):
        """gets the x value
        Returns:
            x (int): value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """sets x value
         Args:
            value(int): x value
        """
        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """gets the y value
        Returns:
            y (int): value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """sets y value
         Args:
            value(int): y value
        """
        if type(value) not in [int]:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

