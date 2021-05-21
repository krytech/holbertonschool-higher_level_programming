#!/usr/bin/python3
"""
A function which prints a text with 2 new lines after:
'.' '?' and ':'
"""


def text_indentation(text):
    """
    Only takes a string and adds 2 new lines after special characters above
    and returns the new string
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    cut_lines = [lines.strip(" ") for lines in text.split("\n")]
    new_version = "\n".join(cut_lines)
    print(new_version, end="")
