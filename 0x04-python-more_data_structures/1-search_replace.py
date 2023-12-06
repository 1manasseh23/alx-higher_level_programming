#!/usr/bin/pyhon3
def search_replace(my_list, search, replace):
    cl_list = []
    for list1 in my_list:
        if list1 == search:
            cl_list.append(replace)
        else:
            cl_list.append(list1)
    return cl_list
