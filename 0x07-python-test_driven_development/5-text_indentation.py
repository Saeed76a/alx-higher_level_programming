#!/usr/bin/python3
"""text"""


def text_indentation(text):
    """
    prints a text
    Args: 
        text (str): text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    for sp in text:
        if sp == ' ':
            i += 1
        else:
            break

    for sp in text:
        print(sp, end="")
        if sp == "\n" or sp in ".?:":
            if sp in ".?:":
                print("\n")
            i = 0
            continue
        elif sp == ' ':
            i += 1
            if i == 2:
                print("\n")
                i = 0
                continue
        i = 0
