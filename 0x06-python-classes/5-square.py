#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        "retrieve/set the size of a Square"
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Printing '#' charater corresponding to square size."""
        if self.size == 0:
            print()
        else:
            i = 0
            while i < self.size:
                a = 0
                while a < self.size:
                    print("#", end="")
                    a += 1
                print()
                i += 1

    def area(self):
        """Return the current square area."""

        return self.__size ** 2
