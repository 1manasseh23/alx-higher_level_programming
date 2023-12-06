#!/usr/bin/pytho3
def common_elements(set_1, set_2):
    print_set = set()
    for setter in set_1:
        if setter in set_2:
            print_set.add(setter)
    return print_set
