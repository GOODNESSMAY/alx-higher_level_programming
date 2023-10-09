#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    may_l = my_list.copy()
    for m in range(0, len(my_list)):
        if my_list[m] % 2 == 0:
            may_l[m] = 1
        else:
            may_l[m] = 0
    return may_l
