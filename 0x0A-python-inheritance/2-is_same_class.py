#!/usr/bin/python3
"""
module that contain function is_same_class
"""


def is_same_class(obj, a_class):

    """return true if object is the exact class a_class, otherwise return false"""
    return (type(obj) == a_class)
