#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    m = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            m += 1
        except(ValueError, TypeError):
            continue
    print()
    return m
