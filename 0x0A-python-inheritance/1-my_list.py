#!/usr/bin/python3

"""
contain MyList class
"""


class MyList(list):

    """subclass of list"""
    def __init__(self):

        """initialization of the object"""
        super().__init__()

    def print_sorted(self):

        """print the sorted list"""
        print(sorted(self))
