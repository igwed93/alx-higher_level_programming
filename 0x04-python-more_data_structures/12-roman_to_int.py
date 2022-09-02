#!/usr/bin/python3
def roman_to_int(roman_string):
    r = roman_string
    if type(r) != str:
        return 0
    elif not r:
        return 0
    rom_num = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10,
               "V": 5, "I": 1, "XC": 90, "XL": 40, "IV": 4,
               "IX": 9, "CM": 900, "CD": 400}
    num = 0
    i = 0

    while i < len(r):
        if i+1 < len(r) and r[i:i+2] in rom_num:
            num += rom_num[r[i:i+2]]
            i += 2
        else:
            num += rom_num[r[i]]
            i += 1

    return (num)
