#!/usr/bin/python3
def roman_to_int(roman_string):
    r_str = roman_string
    if type(r_str) != str:
        return 0
    elif not r_str:
        return 0
    roman_numerals = {"M": 1000, "D": 500, "C": 100, "XL": 40, "L": 50, "IX":
                      9, "X": 10, "IV": 4, "V": 5, "II": 2,
                      "XC": 90, "III": 3, "I": 1}
    sum = 0
    for i in r_str:
        j = r_str.index(i)
        if i in roman_numerals:
            if len(r_str) == 1:
                num = roman_numerals[i]
                sum += num
                return (sum)
            elif i == "I" and r_str[j+1] == "X":
                i = "IX"
                num = roman_numerals[i]
                j = r_str.index(i)
                sum += num
                if len(r_str) == 2:
                    return (sum)
                else:
                    r_str = r_str[:j+2] + r_str[j+2:]
            elif i == "I" and r_str[j+1] == "V":
                i = "IV"
                num = roman_numerals[i]
                sum += num
                if len(r_str) == 2:
                    return (sum)
            elif i == "X" and r_str[j+1] == "L":
                i = "XL"
                num = roman_numerals[i]
                sum += num
                if len(r_str) == 2:
                    return (sum)
            elif i == "X" and r_str[j+1] == "C":
                i = "XC"
                num = roman_numerals[i]
                sum += num
                if len(r_str) == 2:
                    return (sum)
                else:
                    r_str = r_str[:j+2] + r_str[j+2:]
            else:
                num = roman_numerals[i]
                r_str = r_str[:j] + r_str[j+1:]
                sum = sum + num
    return (sum)
