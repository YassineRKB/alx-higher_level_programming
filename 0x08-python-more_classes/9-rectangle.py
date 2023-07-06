#!/usr/bin/python3
"""a class that defines a rectangle"""


class Rectangle:
    """class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init constructor"""
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    def __str__(self):
        """class string"""
        msg = ""
        if self.width == 0 or self.height == 0:
            return msg
        else:
            for i in range(self.height):
                msg += str(self.print_symbol) * self.width
                if i != self.height - 1:
                    msg += "\n"
            return msg

    def __repr__(self):
        """string represetating the class"""
        msg = "Rectangle({}, {})".format(self.width, self.height)
        return msg

    def __del__(slef):
        """on instance delete"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """width property"""
        return self.__width

    @property
    def height(self):
        """height property"""
        return self.__height

    @width.setter
    def width(self, value):
        """width setter"""
        TypeWid = isinstance(value, int)
        if not TypeWid:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        TypeHei = isinstance(value, int)
        if not TypeHei:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area func"""
        return self.height * self.width

    def perimeter(self):
        """preimeter func"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.height + self.width) * 2

    @staticmethod
    def bigger_or_equal(rect1, rect2):
        """a static method"""
        TypeRect1 = isinstance(rect1, Rectangle)
        TypeRect2 = isinstance(rect2, Rectangle)
        if not TypeRect1:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not TypeRect2:
            raise TypeError("rect_2 must be an instance of Rectangle")
        AreaRect1 = Rectangle.area(rect1)
        AreaRect2 = Rectangle.area(rect2)
        if AreaRect1 >= AreaRect2:
            return rect1
        else:
            return rect2

    @classmethod
    def square(cls, size=0):
        """a square class method"""
        return cls(size, size)
