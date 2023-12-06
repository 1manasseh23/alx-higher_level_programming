#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_dict = [me for me, my in a_dictionary.items() if my == value]
    # my_dict = dict(a_dictionary)
    for me in my_dict:
        del a_dictionary[me]
    return a_dictionary
