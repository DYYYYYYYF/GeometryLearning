class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def to_tuple(self):
        return (self.x, self.y)

class Segment:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def to_line(self):
        return (self.p1.to_tuple(), self.p2.to_tuple())

