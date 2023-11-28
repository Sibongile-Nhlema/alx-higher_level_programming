#!/usr/bin/python3
''' Module for the lazy matrix multiplication '''


import numpy as np
''' Function to help with multiplication '''


def lazy_matrix_mul(m_a, m_b):
    ''' multiplies 2 matrices by using the module NumPy '''
    try:
        result = np.matmul(m_a, m_b)
        return result
    except ValueError as e:
        raise ValueError("Matrix multiplication failed: " + str(e))
