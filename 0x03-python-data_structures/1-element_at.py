#!/usr/bin/python3
# 1-element_at.py
# that retrieve element from a list just as in C program.

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
