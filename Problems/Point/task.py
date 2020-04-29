from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, second_point):
        return sqrt((self.x - second_point.x) ** 2 + (self.y - second_point.y) ** 2)
