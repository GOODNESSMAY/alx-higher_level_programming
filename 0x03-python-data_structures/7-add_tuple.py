#!/usr/bin/python3
# 7-add_tuple.py
# to add two tuple program

def add_tuple(tuple_a=(), tuple_b=()):
    lenG = len(tuple_a)
    lenM = len(tuple_b)
# check for tuple_a
    if lenG < 1:
        tuple_a = (0, 0)
    elif lenG < 2:
        tuple_a = (tuple_a[0], 0)

# check for tuple_b
    if lenM < 1:
        tuple_b = (0, 0)
    elif lenM < 2:
        tuple_b = (tuple_b[0], 0)

    res = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return res
