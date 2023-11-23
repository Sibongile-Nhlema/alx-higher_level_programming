#!/usr/bin/python3
''' add_integer() add two intergers 
    add floats but ignoring remainder
    handles TypeErrors
'''

def add_integer(a, b=98):
    ''' Adds two integers.
        Args:
            a: first integer
            b: second integer (initialised to 98)
        Return: Sum of the integers

        >>> add_integer(1, 3)
        4
        >>> add_integer(-2, -6)
        -8
        >>> add_integer(5, -10)
        -5
        >>> add_integer(5.0, 6)
        11
        >>> add_integer(5.3, 1)
        6

    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
