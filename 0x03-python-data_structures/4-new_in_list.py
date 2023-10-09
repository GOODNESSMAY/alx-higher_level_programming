#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    may_list = my_list.copy()
    may_list[idx] = element
    return may_list
