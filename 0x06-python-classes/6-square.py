#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        Initialize a new Square position
        Args:
            position(int, int): The position of the new square
        """
        self.__size = size
        self.__position = position


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

    @property
    def position(self):
        "get/set the position of a Square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Printing '#' charater corresponding to square size."""
        if self.size == 0:
            print()

        [print("") for i in range(0, self.__position[1])]
            
        i = 0
        while i < self.size:
            x = 0
            while x < self.position[0]:
                print(" ",end="")
                x += 1
            a = 0
            while a < self.size:
                print("#", end="")
                a += 1
            print()
            i += 1

    def area(self):
        """Return the current square area."""

        return self.__size ** 2
