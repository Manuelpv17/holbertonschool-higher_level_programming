#!/usr/bin/python3
"""Pascal's Triangle
    """


def pascal_triangle(n):
    """Pascal's Triangle

        Arguments:
                n {int} -- number of iterations

        Returns:
                list -- list of list with pascal triangle
        """
    pascal = []
    if n <= 0:
        return pascal
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(pascal[i - 1][j] + pascal[i - 1][j - 1])
        pascal.append(row)
    return pascal
