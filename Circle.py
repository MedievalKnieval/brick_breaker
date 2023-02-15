import math

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return ((self.r ** 2) * math.pi)

    def get_diameter(self):
        return (2 * self.r)