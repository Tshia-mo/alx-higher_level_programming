#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            to_sub += n

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0
