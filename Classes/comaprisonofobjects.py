class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    #comparing object using magic method
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    #checking the greater value between two object  using gt magic method
    def __gt__(self,other):
        return self.x > other.x and self.y > other.y
     


    def draw(self):
        print(f"just like always ({self.x}, {self.y})")
point = Point(40,50)
point.draw()
other = Point(4,5)
other.draw()
print(point == other)
print(point > other)