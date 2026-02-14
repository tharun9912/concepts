
""" Polymorphism , overriding methods """

class Shape:
    def area(self):
        print("Area calculation")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of Circle:", 3.14 * self.radius * self.radius)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area of Square:", self.side * self.side)

if __name__=="__main__":
    sh=Shape()
    ci=Circle(8)
    sq = Square(6)

    sh.area()
    ci.area()
    sq.area()

