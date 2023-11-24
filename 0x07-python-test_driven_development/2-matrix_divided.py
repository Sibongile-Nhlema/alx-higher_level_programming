#!/usr/bin/python3
''' Module for matrix_divided
    a function that divides all elements of a matrix.
    raises error if inputs are not of type int/float
'''

def matrix_divided(matrix, div):
    ''' Args:
            matrix: lists of lists that have int/floats
            div: the divisor int/float
        Return: a new matrix with divided values
    '''
    new_matrix = []
    if len(matrix) == 0:
        raise TypeError("matrix_divided() missing 1 required positional argument: 'matrix'")
    if any(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if matrix is None or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div is None:
        raise TypeError("div must be a number")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in range(len(matrix)):
        if not isinstance(matrix[row], list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[row]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for element in range(len(matrix[row])):
            if not isinstance(matrix[row][element], int) and not isinstance(matrix[row][element], float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_element = round(matrix[row][element] / div, 2)
            new_list.append(new_element)
        new_matrix.append(new_list)
    return new_matrix
