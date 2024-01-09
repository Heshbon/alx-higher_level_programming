#!/usr/bin/python3
"""defines from json string module"""


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    import json
    return json.loads(my_str)
