#!/usr/bin/python3

"""
Definition of a class Rectangle
"""


class Rectangle:

    """Rep of a rectangle"""

    def __init__(self, width=0, height=0):

        """Initializes the rectangle"""

        self.height = height
        self.width = width

    @property """The @property decorator is used to define a getter method for the height attribute. A getter method is used to get the value of an attribute.In this case, the height attribute can be accessed using the .height syntax."""
