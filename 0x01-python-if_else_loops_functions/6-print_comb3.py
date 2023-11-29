#!/usr/bin/python3

for cleta in range(10):
    for vivan in range(cleta + 1, 10):
        print("{:d}{:d}".format(cleta, vivan), end=", " if cleta != 8\
                or vivan != 9 else "\n")
