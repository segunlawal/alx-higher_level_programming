#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    new_list = []
    for char in str_list:
        if char != "c" and char != "C":
            new_list.append(char)
    str = "".join(new_list)
    return str
