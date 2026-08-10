#!/usr/bin/python3
"""Divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide a matrix by div and round to 2 decimal places."""
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if any(not isinstance(x, (int, float)) or isinstance(x, bool)
           for row in matrix for x in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if matrix:
        size = len(matrix[0])
        if any(len(row) != size for row in matrix):
            raise TypeError(
                "Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
