#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        if ord('a') <= ord(ch) <= ord('Z'):
            print(chr(ord(ch) - (ord('a') - ord('A'))), end="")
        else:
            print("{}".format(ch), end="")
    print()

