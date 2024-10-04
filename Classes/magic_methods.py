class Point:
    def __init__(self,x,y):
        self.y = y
        self.x = x
    #magic method of  adding
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __eg__(self,other):
        return Point(self.x and other.x > self.y and other.y)

    def draw(self):
        print(f"welcome to our online logic state({self.x},{self.y})")

point = Point(23,8)
point.draw()
other  = Point(5,8)
other.draw()
#printing combination of the two objects
combine = point + other
print(f"here is the combine of them both ({combine.x},{combine.y})")
#comparison bteween two
compare = Point(30,30)
compare.draw()
other = Point(20,15)
other.draw()
coparing = (compare == other)
print(coparing)



