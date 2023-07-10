#!/usr/bin/python3
"""
12. My integer
"""


class MyInt(int):
    """
    a rebel of int
    """
    def __eq__(self, other):
        """
        override the default behavior of ==
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        override the default behavior of !=
        """
        return super().__eq__(other)
