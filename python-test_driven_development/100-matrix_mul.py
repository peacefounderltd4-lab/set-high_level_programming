#!/usr/bin/python3
"""
Module for matrix_mul function.
This module provides a function to multiply two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b.

    Args:
        m_a (list of lists of int/float): First matrix.
        m_b (list of lists of int/float): Second matrix.

    Returns:
        list of lists: The multiplied matrix.

    Raises:
        TypeError: If m_a or m_b is not a list or list of lists.
        ValueError: If m_a or m_b is empty.
        TypeError: If elements are not integers or floats.
        TypeError: If rows are not of equal size.
        ValueError: If m_a and m_b cannot be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for ele in row:
            if type(ele) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for ele in row:
            if type(ele) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    first_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != first_len_a:
            raise TypeError("each row of m_a must be of the same size")

    first_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != first_len_b:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            sum_val = 0
            for k in range(len(m_b)):
                sum_val += m_a[i][k] * m_b[k][j]
            new_row.append(sum_val)
        result.append(new_row)

    return result
