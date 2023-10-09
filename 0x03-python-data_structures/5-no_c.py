#!/usr/bin/python3
# 5-n0_c.py
def no_c(my_string):
    may_s = my_string.translate({ord('c'): None})
    may_s = may_s.translate({ord('C'): None})
    return may_s
