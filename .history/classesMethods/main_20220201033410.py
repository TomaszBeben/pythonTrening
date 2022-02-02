import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = math.sqrt(x**2 + y**2)

    def __add__(self, z):
        return Point2D(self.x + z.x, self.y + z.y)

    def __lt__(self, sec):
        return self.distance < sec.distance
        
    def __eq__(self, sec):
        return self.distance

p1 = Point2D(2, 5)
p2 = Point2D(4, 5)
p3 = p1 + p2

print(p3.x)
print(p3.y)

print(p1 < p2)
print(p1 > p2)
print(p1.distance)
print(p2.distance)
