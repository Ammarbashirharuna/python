class Point:
    #adding a constructor
    def __init__(self, x,y):
        self.x = x
        self.y = y


    def draw(self):
        print(f"{self.x}, {self.y} this is a constructor")

point = Point(1,3)
draw = point.draw()
#drawing another point to a terminal
anoth_point = Point(3,5)
anoth_point.draw()
#another
another = Point(4,5)
another.draw()







