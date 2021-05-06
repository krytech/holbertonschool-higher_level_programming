#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    next = ""
    for i in range(len(roman_string)):
        if roman_string[i] in dict.keys():
            val = roman_string[i]
            if i < len(roman_string) - 1:
                next = roman_string[i + 1]
            if i == len(roman_string) - 1:
                sum += dict[val]
            elif dict[val] < dict[next]:
                sum -= dict[val]
            else:
                sum += dict[val]
    return sum
