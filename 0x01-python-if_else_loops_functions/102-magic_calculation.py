#!/usr/bin/python3
import dis
def magic_calculation(a, b, c):
    if not (a < b):
        return (c)
    if not (c > b):
        return (a + b)
    return (a * b - c)
