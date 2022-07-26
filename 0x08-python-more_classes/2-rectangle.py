#!/usr/bin/python3
""" 2-rectangle

    Class Rectangle
    area method
    perimeter method

    Raises:
        TypeError: height must be an integer
        ValueError: height must be >= 0
        TypeError: width must be an integer
        ValueError: width must be >= 0
"""


class Rectangle():
    """Rectangle Class

    Class with Width and height properties
    """

    def __init__(self, width=0, height=0):
        """__init__ constructor

        Contructor of Rectangle class

        Args:
            width (int, optional): Width by Rectangle. Defaults to 0.
            height (int, optional): Height by Rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """height Getter

        Get height value

        Returns:
            int: height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height Setter

        Set height value

        Args:
            value (int): value to set

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        """width Getter

        Get width value

        Returns:
            int: width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width Setter

        set width value

        Args:
            value (int): value to set

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    def area(self):
        """area Method

        rectangle area

        Returns:
            int: rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """perimeter Method

        rectangle perimeter

        Returns:
            int: rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__height + self.__width)
