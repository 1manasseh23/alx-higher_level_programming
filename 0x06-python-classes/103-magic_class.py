"""
This line imports the math module, which provides
mathematical functions and constants, including pi
"""


import math
"""
This line begins the definition of the MagicClass class.
"""


class MagicClass:
    """
    This initializes the class instance and sets a
    private attribute __radius to 0 by default.
    Attribute:
        radius
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
    """
    This method calculates and returns the area of the circle
    using the formula pi * radius^2, where pi is the mathematical
    constant obtained from the math module.
    Attribute:
        __radius
    """
    def area(self):
        return self.__radius ** 2 * math.pi
    """
    This method calculates and returns the circumference of the
    circle using the formula 2 * pi * radius, where pi is the
    mathematical constant obtained from the math module.
    Attribute:
        __radius
    """
    def cicumference(self):
        return 2 * math.pi * self.__radius
