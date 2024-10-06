from collections import namedtuple
class Point:
    def __init__(self, x,y):
       self.x = x
       self.y = y

    def __eg__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1,2)
p2 = Point(1,2)
print(p1 == p2)


#using named tuple and its more easier and concise
Point =  namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=1)
p2 = Point(x=1, y=1)
print(p1 == p2)
