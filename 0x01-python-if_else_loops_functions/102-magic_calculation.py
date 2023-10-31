#!/usr/bin/python3
import dis


def magic_calculation(a, b, c):
    if not (a < b):
        return (c)
    elif not (c > b):
        return (a + b)
    else:
        return (a * b - c)
