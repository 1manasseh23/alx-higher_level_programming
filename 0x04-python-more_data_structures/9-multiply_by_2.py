#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    retn_dic = {}
    for ky, value in a_dictionary.items():
        retn_dic[ky] = value * 2
    return retn_dic
