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
    if matrix is None:
        raise TypeError("matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'")
    if isinstance(div, (int, float)):
        if div == 0:
            raise ZeroDivisionError("division by zero")
        for row in range(len(matrix) - 1):
            if len(matrix[row]) != (len(matrix[row + 1])):
                raise TypeError("Each row of the matrix must have the same size")
        for row in range(len(matrix)):
            if row is None:
                TypeError("Each row of the matrix must have the same size")
            new_list = []
            for element in range(len(matrix[row])):
                if isinstance(element, (int, float)):
                    new_element = round(matrix[row][element] / div, 2)
                    new_list.append(new_element)
                else:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix.append(new_list)
        return new_matrix
    else:
        raise TypeError("div must be a number")
