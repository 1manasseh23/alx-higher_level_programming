#!/usr/bin/python3
for exception in range(100):
    print("{:02d}".format(exception), end=", " if exception != 99 else "\n")
