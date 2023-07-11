#!/usr/bin/python3
"""
 0. Read file
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8)
    and prints it to stdout:

    Args:
        filename (str): tha name of the file to read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
    for line in read_data:
        print(line, end='')
