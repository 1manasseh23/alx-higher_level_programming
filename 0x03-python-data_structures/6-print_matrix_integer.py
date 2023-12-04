#!/usr/bin/python3
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for number in range(len(matrix[row])):
                if number != len(matrix[row]) - 1:
                    endspace = " "
                else:
                    endspace = " "
                print("{:d}".format(matrix[row][number]), end=endspace)
            print()
