#!/usr/bin/python3
"""
13. Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename (str): the file name
        search_string (str): the string we looking for
        new_string (str): the appended string
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = []
        while True:
            line_read = file.readline()
            if line_read == "":
                break
            lines.append(line_read)
            if search_string in line_read:
                lines.append(new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)
