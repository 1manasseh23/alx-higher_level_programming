#!/usr/bin/python3

def pow(a, b):
    output = 1
    if b < 0:
        a = 1 / a
        b = abs(b)

    for _ in range(b):
        output *= a

    return output
