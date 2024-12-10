class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x, self.y})"


p1 = Point(2, 3)
p2 = Point(3, 4)
print(p1)
print(p2)
p3 = p1 + p2 # triggers the __add__ dunder/magic method
print(p3) # trigger __str__ dunder/magic method