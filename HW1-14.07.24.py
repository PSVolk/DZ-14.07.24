import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Circle(self.radius + other)
        elif isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Circle' and '{}'".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Circle(self.radius - other)
        elif isinstance(other, Circle):
            return Circle(self.radius - other.radius)
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Circle' and '{}'".format(type(other).__name__))

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.radius += other
        elif isinstance(other, Circle):
            self.radius += other.radius
        else:
            raise TypeError("Unsupported operand type(s) for +=: 'Circle' and '{}'".format(type(other).__name__))
        return self

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            self.radius -= other
        elif isinstance(other, Circle):
            self.radius -= other.radius
        else:
            raise TypeError("Unsupported operand type(s) for -=: 'Circle' and '{}'".format(type(other).__name__))
        return self

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

circle1 = Circle(5)
circle2 = Circle(10)


print(circle1 == circle2)
print(circle1 == Circle(5))


print(circle1 < circle2)
print(circle1 > circle2)
print(circle1 <= circle1)
print(circle1 >= circle2) 


circle3 = circle1 + 3
print(circle3.radius)
circle3 -= 2
print(circle3.radius)
circle3 += circle2
print(circle3.radius)

print(circle1.area())
print(circle1.circumference())
