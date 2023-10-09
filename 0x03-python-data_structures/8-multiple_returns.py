#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        outcome = (0, None)
        return outcome
    else:
        outcome = (length, sentence[0:1])
        return outcome
