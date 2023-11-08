#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    prev_numeral = 0
    roman_numerals_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    if type(roman_string) != str or roman_string is None:
        return None

    for i in range(len(roman_string)):
        if roman_string[i] in roman_numerals_dict:
            current_numeral = roman_numerals_dict[roman_string[i]]
            if prev_numeral < current_numeral:
                num -= 2 * prev_numeral
            num += current_numeral
            prev_numeral = current_numeral

    return num
