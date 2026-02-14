from abc import ABC, abstractmethod

# Parent Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Child Class 1
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# Child Class 2
class Rectangle(Shape):

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


# Function that works with Parent type
def print_area(shape):
    print("Area:", shape.area())


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(8, 12)

    print_area(circle)      
    print_area(rectangle)
