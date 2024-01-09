#!/usr/bin/python3
"""defines load from json file module"""


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""
    import json
    with open(filename, 'r') as f:
        return json.loads(f.read())
