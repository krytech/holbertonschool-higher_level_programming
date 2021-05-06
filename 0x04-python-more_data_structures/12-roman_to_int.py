#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    for i in range(len(roman_string)):
        if roman_string[i] in dict.keys():
            val = roman_string[i]
            sum += dict[val]
    return sum
