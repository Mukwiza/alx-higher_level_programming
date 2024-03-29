#!/usr/bin/python3
"""first Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """rectangle class that inherits from the base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructs the rectange's attributes"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the Width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the Width  of the rectangle"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the height of the rectangle"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """gets the x value"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets x value"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """gets the y value"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets y value"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        '''returns the area value of rectangle'''
        return (self.height*self.width)

    def display(self):
        '''print rectangle instance in stdout using # character'''
        for line in range(self.__y):
            print()
        for height in range(self.__height):
            for space in range(self.__x):
                print(' ', end='')
            for width in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """str method to return rectangle representation"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        '''assigning an argument to each attribute'''
        if args is not None:
            arg_list = []
            for arg in args:
                arg_list.append(arg)
            i = 0
            while i < len(arg_list):
                if i == 0:
                    self.id = arg_list[i]
                elif i == 1:
                    self.__width = arg_list[i]
                elif i == 2:
                    self.__height = arg_list[i]
                elif i == 3:
                    self.__x = arg_list[i]
                elif i == 4:
                    self.__y = arg_list[i]
                i += 1

        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of Rectangle'''
        dic = {'x': self.__x,
               'y': self.__y,
               'id': self.id,
               'height': self.__height,
               'width': self.__width}
        return dic
