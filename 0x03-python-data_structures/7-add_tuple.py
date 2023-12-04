#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_tuple1 = tuple_a + (0, 0)
    my_tuple2 = tuple_b + (0, 0)
    val = (my_tuple1[0] + my_tuple2[0], my_tuple1[1] + my_tuple2[1])
    return(val)
