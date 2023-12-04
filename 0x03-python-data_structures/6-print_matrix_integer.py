#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return

    for prt_max in matrix:
        for trx in enumerate(prt_max):
            if trx < len(prt_max) - 1:
                print("{:d}".format(prt_max[trx]), end="")
            else:
                print("{:d}".format(prt_max[trx]), end="")
        print()
