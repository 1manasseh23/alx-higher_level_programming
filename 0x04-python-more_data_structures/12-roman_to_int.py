#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom_nums = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
    }
    rom = 0
    re_val = 0

    for char in reversed(roman_string):
        val = rom_nums[char]
        if val >= re_val:
            rom += val
        else:
            rom -= val
        re_val = val
    return rom
