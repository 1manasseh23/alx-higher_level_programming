#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return_set = set()
    for cl in set_1:
        if cl not in set_2:
            return_set.add(cl)
    for cl in set_2:
        if cl not in set_1:
            return_set.add(cl)
    return return_set
