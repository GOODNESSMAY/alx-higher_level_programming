#!/usr/bin/python3
# 9-print_last_digit
def print_last_digit(number):
    '''print last digit of a number and return last digit'''
    last_digit = abs(number) % 10
    print(f"{last_digit}", end='')
    return last_digit
