#!/usr/bin/python3
"""Implementing a Geometry class.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represents rectangle.
    """

    def __init__(self, width, height):
        """initialize data.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Implementing area."""
        return (self.__width * self.__height)

    def __str__(self):
        """Print."""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
