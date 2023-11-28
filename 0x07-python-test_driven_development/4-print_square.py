#!/usr/bin/python3
''' print_square() prints a square
    return an error if the input is not an integer or a float
    '''


def print_square(size):
    ''' Args:
            size(int/float): size of the square
    '''
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if type(size) == "float" and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        size = int((size // 1))
    for row in range(size):
        for column in range(1, size):
            print("#", end="")
        print("#")
