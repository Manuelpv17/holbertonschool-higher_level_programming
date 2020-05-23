#!/usr/bin/python3
"""multiplies 2 matrices

    """


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices

    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    columns_a = len(m_a[0])
    for row_a in m_a:
        if type(row_a) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(row_a) != columns_a:
            raise TypeError("each row of m_a must be of the same size")
        for item in row_a:
            if type(item) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    columns_b = len(m_b[0])
    for row_b in m_b:
        if type(row_b) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(row_b) != columns_b:
            raise TypeError("each row of m_b must be of the same size")
        for item in row_b:
            if type(item) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    mul = []
    for i in range(len(m_a)):
        row = []
        for n in range(len(m_b[0])):
            sum = 0
            for m in range(len(m_a[0])):
                sum += m_a[i][m] * m_b[m][n]
            row.append(sum)
        mul.append(row)
    return mul
