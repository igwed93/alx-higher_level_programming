#!/usr/bin/python3
"""script that adds all arguments to a Python list,
   and then save them to a file
Args:
    add_item.json: file
Modlues:
    save_too_json_file
    load_from_json_file
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"

    try:
        previous_content = load_from_json_file(filename)
    except Exception as e:
        previous_content = []

    save_to_json_file(previous_content + argv[1:], filename)
