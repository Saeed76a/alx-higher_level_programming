#!/usr/bin/python3
"""
My Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    the class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the object with the provided arguments.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): x point of width
            y (int): y point of height
            id (int): attribute's id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """
    define width
    """
    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        Args:
            value (int): the value of width
        Raise:
            TypeError with message
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """
    define height
    """
    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Args:
            value (int): the value of height
        Raise:
            TypeError with message
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """
    define x
    """
    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        Args:
            value (int): the value of x
        Raise:
            TypeError with message
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """
    define y
    """
    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        Args:
            value (int): the value of y
        Raise:
            TypeError with message
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        get the area
        value of the Rectangle

        Return:
            the area
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the Rectangle
        """
        for i in range(self.height + self.y):
            for j in range(self.width + self.x):
                if i >= self.y and j >= self.x:
                    print("{}".format("#"), end='')
                elif i < self.y:
                    print("", end="")
                else:
                    print(" ", end="")
            print("")

    def __str__(self):
        """
        get the rectangle's info
        """
        return "[Rectangle] ({}) {}/{} - {}/{}\
".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Update method
        """
        i = 0
        if not args:
            for attri in kwargs:
                if attri == "id":
                    super().__init__(kwargs[attri])
                if attri == "width":
                    self.width = kwargs[attri]
                if attri == "height":
                    self.height = kwargs[attri]
                if attri == "x":
                    self.x = kwargs[attri]
                if attri == "y":
                    self.y = kwargs[attri]

        for arg in args:
            if i == 0:
                super().__init__(arg)
            elif i == 1:
                self.width = arg
            elif i == 2:
                self.height = arg
            elif i == 3:
                self.x = arg
            elif i == 4:
                self.y = arg
            i += 1
