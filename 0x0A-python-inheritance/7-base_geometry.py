#!/usr/bin/python3
"""Modulez: 7-base_geometry
"""


class BaseGeometry:
    """Represents BaseGeometry class.
    """

    def area(self):
        """Not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value validation.
        Args:
            name (str): name of parameter
            value (int): parameter to validate.
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
