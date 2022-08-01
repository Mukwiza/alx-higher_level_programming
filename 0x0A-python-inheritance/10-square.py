#!/usr/bin/python3
"""Implementing a Geometry class."""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents Square class."""

    def __init__(self, size):
        """initialize data."""
        self.integer_validator("size", size)
        
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """Print."""
        return ("[Rectangle] " + str(self.__size) + "/" + str(self.__size))
