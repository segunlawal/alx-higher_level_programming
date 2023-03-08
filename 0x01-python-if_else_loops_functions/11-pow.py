#!/usr/bin/python3
def pow(a, b):
    exp = 1
    c = b
    if c < 0:
        c *= -1
    for i in range(c):
        exp *= a
    if b < 0:
        exp = 1/exp
    return exp
