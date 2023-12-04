#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_mul = []

    for numbs in my_list:
        my_mul.append(numbs % 2 == 0)
    return my_mul
