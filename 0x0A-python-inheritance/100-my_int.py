#!/usr/bin/python3
"""
MyInt is a class that inherits from int
Attribute:
    int
"""


class MyInt(int):
    """
    This function defines a rebel integer
    Attribute:
        other
    """
    def __eq__(self, other):
        """
        Inverts the == operator
        """
        return super().__ne__(other)

    """
    This function overridden to invert the operator
    Attribute:
        other
    """
    def __ne__(self, other):
        """
        Inverts the != operator
        """
        return super().__eq__(other)
