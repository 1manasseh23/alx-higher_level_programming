#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    output_list = []
    for j in range(list_length):
        try:
            if j < len(my_list_1) and j < len(my_list_2):
                output = my_list_1[j] / my_list_2[j]
            else:
                raise IndexError("out of range")
        except TypeError:
            print("wrong type")
            output = 0
        except ZeroDivisionError:
            print("division by 0")
            output = 0
        except IndexError as e:
            print(e)
            output = 0
        finally:
            output_list.append(output)
    return output_list
