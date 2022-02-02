import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = math.sqrt(x**2 + y**2)

    def __add__(self, z):
        return Point2D(self.x + z.x, self.y)

p1 = Point2D(2, 5)
p2 = Point2D(4, 5)
p3 = p1 + p2


