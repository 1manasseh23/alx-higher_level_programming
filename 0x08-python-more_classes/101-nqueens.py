#!/usr/bin/python3
"""
Imports the sys module which provides access to
some variables used or maintained
"""


import sys
"""
Checks conditions for the safety of placing a queen at a
particular position on the board. It compares
Attribute:
    board
    row
    col
    n
"""


def is_safe(board, row, col, n):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


"""
Defines a function solve_n_queens that recursively
finds solutions for the N-Queens problem
Attribute:
    n
    board
    col
    solutions
"""


def solve_n_queens(n, board, col, solutions):
    if col == n:
        solutions.append(board[:])
        return
    for row in range(n):
        if is_safe(board, row, col, n):
            board[col] = row
            solve_n_queens(n, board, col + 1, solutions)


"""
Defines a function print_solutions to print the
solutions in a specific forma
Attribute:
    n
    solutions
"""


def print_solutions(n, solutions):
    for solution in solutions:
        print("[", end="")
        for i in range(n):
            print("[{}, {}]".format(i, solution[i]), end="")
            if i != n - 1:
                print(", ", end="")
        print("]")


"""
Checks if the script is being run as the main program
"""


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    solutions = []
    solve_n_queens(n, board, 0, solutions)
    print_solutions(n, solutions)
