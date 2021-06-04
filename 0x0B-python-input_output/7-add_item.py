#!/usr/bin/python3
""" A script that adds all arguments to a Python list """


from sys import argv
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

try:
    json_list = load_from_json("add_item.json")
except FileNotFoundError:
    json_list = []

save_to_json(json_list + argv[1:], "add_item.json")
