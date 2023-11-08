#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    roman_numerals_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if type(roman_string) != str:
        return None
    for i in range(len(roman_string)):
        if roman_string[i] in roman_numerals_dict:
            if roman_string[i] == "X" and roman_string[i - 1] == "I":
                num -= 2
            if roman_string[i] == "M" and roman_string[i - 1] == "C":
                num -= 200
            num += roman_numerals_dict[roman_string[i]]
    return num
