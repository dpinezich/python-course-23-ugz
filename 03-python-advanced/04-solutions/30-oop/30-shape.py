import math


class Shape:
    def area(self):
        raise NotImplementedError("Cannot calculate area of a general shape")

    def circumference(self):
        raise NotImplementedError(
            "Cannot calculate the circumference of a general shape."
        )

    def __str__(self):
        return "Shape Class"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return "Circle"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def circumference(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return "Rectangle"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def __str__(self):
        return "Square"


if __name__ == "__main__":
    square = Square(5)
    print(square.area())

    shapes = [Circle(3), Rectangle(3, 4), Square(2)]
    for shape in shapes:
        print(shape)
        print("Area: ", shape.area())
        print("Circumference:", shape.circumference())
        print("**********")
        print()

shape = Shape()
print(shape)
