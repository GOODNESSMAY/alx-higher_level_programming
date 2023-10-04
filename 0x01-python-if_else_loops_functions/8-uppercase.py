#!/usr/bin/python3
# 8-uppercase.py
def uppercase(str):
    for og in str:
        if ord(og) >= 97 and ord(og) <= 122:
            og = chr(ord(og) - 32)
        print("{:s}".format(og), end='')

    print('\n', end="")
