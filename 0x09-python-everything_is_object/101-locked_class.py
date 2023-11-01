#!/usr/bin/python3

# 101-locked_class.py

"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
