#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mul_matrix = []
    for cl in matrix:
        new_cl = []
        for elnt in cl:
            new_cl.append(elnt ** 2)
        mul_matrix.append(new_cl)
    return mul_matrix
