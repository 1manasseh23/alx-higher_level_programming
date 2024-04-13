#!/bin/python3
def find_peak(list_of_integers):
    n = len(list_of_integers)
    if n == 0:
        return None

    if list_of_integers[0] >= list_of_integers[1]:
        return 0

    if list_of_integers[n - 1] >= list_of_integers[n - 2]:
        return n - 1
    left, right = 1, n - 2

    while left <= right:
        mid = left + (right - left) // 2

        if list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:
            return mid

        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            right = mid - 1
        else:
            left = mid + 1

    return None
