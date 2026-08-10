#!/usr/bin/python3
"""Multiply two matrices."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if (not all(isinstance(row, list) for row in m_a)):
        raise TypeError("m_a must be a list of lists")

    if (not all(isinstance(row, list) for row in m_b)):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not all(m_a):
        raise ValueError("m_a can't be empty")

    if not m_b or not all(m_b):
        raise ValueError("m_b can't be empty")

    if any(not isinstance(x, (int, float)) or isinstance(x, bool)
           for row in m_a for x in row):
        raise TypeError(
            "m_a should contain only integers or floats")

    if any(not isinstance(x, (int, float)) or isinstance(x, bool)
           for row in m_b for x in row):
        raise TypeError(
            "m_b should contain only integers or floats")

    a_size = len(m_a[0])
    b_size = len(m_b[0])

    if any(len(row) != a_size for row in m_a):
        raise TypeError(
            "each row of m_a must be of the same size")

    if any(len(row) != b_size for row in m_b):
        raise TypeError(
            "each row of m_b must be of the same size")

    if a_size != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []

    for row in m_a:
        new_row = []

        for j in range(len(m_b[0])):
            value = 0

            for i in range(len(m_b)):
                value += row[i] * m_b[i][j]

            new_row.append(value)

        result.append(new_row)

    return result
