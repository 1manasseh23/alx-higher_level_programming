#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return

    for jack in matrix:
        for y in range(len(jack)):
            if y == len(jack) - 1:
                print("{:d}".format(jack[y]), end="")
            else:
                print("{:d}".format(jack[y]), end=" ")
        print()
