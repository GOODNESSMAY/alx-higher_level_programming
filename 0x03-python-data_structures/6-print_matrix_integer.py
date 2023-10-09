#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    for g in matrix:
        print(" ".join("{:d}".format(m) for m in g))
