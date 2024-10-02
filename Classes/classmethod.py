class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    @classmethod
    def zero(cls):
        return cls(0,0)

    def draw(self):
        print(f"Points ({self.x},{self.y}) are the point")

point = Point(1,5)
point.draw()

point = Point.zero()
point.draw()
