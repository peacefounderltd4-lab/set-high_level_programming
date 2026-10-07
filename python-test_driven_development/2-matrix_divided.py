#!/usr/bin/python3
"""
Module for matrix_divided function.
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): Matrix containing integers or floats.
        div (int or float): Number to divide by.

    Returns:
        list of lists: A new matrix with rounded results to 2 decimal places.

    Raises:
        TypeError: If matrix elements/structure or div are invalid.
        ZeroDivisionError: If div is zero.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for ele in row:
            if type(ele) not in (int, float):
                raise TypeError(msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("matrix must have each row with the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(ele / div, 2) for ele in row] for row in matrix]
