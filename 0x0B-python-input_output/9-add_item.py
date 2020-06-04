#!/usr/bin/python3
"""Load, add, save
    """
from sys import argv
import json

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    prev = load_from_json_file("add_item.json")
except:
    prev = []
for elem in argv[1:]:
    prev.append(elem)
save_to_json_file(prev, "add_item.json")
