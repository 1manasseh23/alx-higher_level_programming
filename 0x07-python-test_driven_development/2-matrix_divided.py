#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a give number.

    Args:
    matrix (list): A list of lists of integers or floats.
    div (int or float): A number to divide the matrix elements by.

    Return:
    list: A new matrix with all elements divided by div and rounded to 2 decimal pleces.

    Raise:
    TypeError: If matrix is not a list of lists of integers or floats, or if div is not an integer or float.
    TypeError: If each row of the matrix is noe the same size.
    ZeroDivisionError: If div is equal to 0.
    """
    if type(matrix) != list or not all(isinstance(row, list) for row in matrix) or not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
