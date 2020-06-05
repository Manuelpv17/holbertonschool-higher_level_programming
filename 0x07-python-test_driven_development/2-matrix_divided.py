#!/usr/bin/python3
"""function that prints My name is <first name> <last name>
    """


def matrix_divided(matrix, div):
    """[summary]

        Arguments:
                matrix {int, float} --
                matrix to be divided
                div {int, float} -- division number

        Raises:
                TypeError: matrix must be a
                matrix (list of lists) of integers/floats
                ZeroDivisionError: division by zero
                TypeError: Each row of the matrix must have the same size
                TypeError: div must be a number

        Returns:
                [type] -- [description]
        """
    new = []
    if type(div) not in [int, float]:
        raise TypeError(
            "div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    size = len(matrix[0])
    for row in matrix:
        new_row = []
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix(list of lists) of integers/floats")
        if size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(item / div, 2))
        new.append(new_row)
    return new
