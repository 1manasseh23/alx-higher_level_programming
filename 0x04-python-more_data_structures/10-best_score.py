#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        my_big_val = max(a_dictionary, key=a_dictionary.get)
        return my_big_val
    else:
        return None
