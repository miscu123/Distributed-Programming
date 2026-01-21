import math


class Shape:
    def area(self):
        return "Area"


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be > 0")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return "Circle with radius " + str(self.radius) + " has area " + str(round(self.area(), 2))


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Length / width must be > 0")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return "Rectangle with width " + str(self.width) + " and height " + str(self.height) + " has area " + str(self.area())


circle = Circle(5)
rectangle = Rectangle(10, 4)
square = Rectangle(5, 5)
print(circle)
print(rectangle)
print(square)