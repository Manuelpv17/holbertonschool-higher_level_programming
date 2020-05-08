#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for row in matrix:
        r = []
        for item in row:
            r.append(item ** 2)
        m.append(r)
    return(m)
