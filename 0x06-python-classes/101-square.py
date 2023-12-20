#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
                not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(j, int) for j in value)
                or not all(j >= 0 for j in value)
                ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        square_representation = ""
        if self.__size == 0:
            square_representation += "\n"
        else:
            for _ in range(self.__position[1]):
                square_representation += "\n"
            square_representation = ""
            for _ in range(self.__size):
                line = " " * self.__position[0] + "#" * self.__size + "\n"
                square_representation += line
            return square_representation.rstrip()
