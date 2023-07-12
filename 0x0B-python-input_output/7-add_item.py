#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""
    This function reads from stdout (cmd line args) then convert
    to a json object in a specified file
"""


if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        item = load_from_json_file("add_item.json")
        item.extend(argv[1:])
        save_to_json_file(item, "add_item.json")
    else:
        save_to_json_file([], "add_item.json")
