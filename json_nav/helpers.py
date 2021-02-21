'''
Helper functions for json.navigation.py
'''
import json


def read_file(path: str) -> dict:
    """
    Read the data from a file and return it
    """
    with open(path) as file:
        data = json.load(file)
    
    return data

