#!/usr/bin/python3
"""First rectangle class"""


from models.base import Base


class Rectangle(Base):
    """rectangle class that inherits from the base class
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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the Width of the rectangle.
        Returns:
            width(int): value of width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """sets the Width  of the rectangle
        Args:
            width(int): value of the rectangle
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """gets the height of the rectangle
        Returns:
            height(int): value fo height
        """
        return self.__height

    @width.setter
    def height(self, height):
        """sets the height of the rectangle
          Args:
            height(int): value of the rectangle
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """gets the x value
        Returns:
            x(int): value of x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """sets x value
         Args:
            x(int): x value
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """gets the y value
        Returns:
            y(int): value of y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """sets y value
         Args:
            y(int): y value
        """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
