#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    for char in str_list:
        if char == "c" or char == "C":
            str_list.remove(char)
    str = "".join(str_list)
    return str
