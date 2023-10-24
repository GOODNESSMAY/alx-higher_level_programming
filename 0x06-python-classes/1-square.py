#!/usr/bin/python3

"""Square class defined"""


class Square:
    """Rep a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initialize a square
        Args:
            size (int): size of a side of the square
        returns: None
        """
        self.__size = size
