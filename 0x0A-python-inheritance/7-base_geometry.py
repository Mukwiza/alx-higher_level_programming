#!/usr/bin/python3
"""Modulez: 7-base_geometry
"""


class BaseGeometry:
    """Represents BaseGeometry class.
    """

    def __init__(self, name=None, value=None):
        """Initialize data.
        """
        self.name = name
        self.value = value

    def area(self):
        """Not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value validation.
        """
        BaseGeometry.__init__(self, name, value)

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
