#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    big = my_list[0]
    for m in range(1, len(my_list)):
        if big < my_list[m]:
            big = my_list[m]
        else:
            continue
    return big
