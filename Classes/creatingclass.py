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

#creating new class car
class Car:
    def __init__(self, model,year):
        self.model = model
        self.year = year
    def starting_engine(self):
        print(f"your car {self.model} has been out since {self.year}")

my_car = Car("Toyota", "2023")
my_car.starting_engine()

#calling method
my_new_car = Car("Audie","2024")
my_new_car.starting_engine()




#creating human class
class Man:
    #class attribute
    default_skin_color = "black"
    def __init__(self, skin, ismarried):
        self.skin = skin
        self.ismarried = ismarried
    
    def  man_details(self):
        print(f"it seems your skin is {self.skin} and you are not maried {self.ismarried}")

black_man = Man("black","yes")
#accessing class attribute
print(Man.default_skin_color)
black_man.man_details()

white_man = Man("white", "no")
white_man.man_details()





