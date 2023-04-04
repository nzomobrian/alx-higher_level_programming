#!/usr/bin/python3
"""
This module has a simple rectangle class
"""


class Rectangle:
    """Basic rectangle with width and height"""
    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional height and width"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for rectangle width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for rectangle height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function to get the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Function to get the perimeter of the rectangle"""
        if self.width is 0 or self.height is 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        ret = ""
        if self.height is 0 or self.width is 0:
            return ret
        for x in range(self.height):
            ret += str(Rectangle.print_symbol) * self.width \
                    + ("\n" if x != self.height - 1 else "")
        return ret

    def print(self):
        print(str(self))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

