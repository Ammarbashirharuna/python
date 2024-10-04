class Animal:
    def __init__(self):
        print("thats good as well know it seems anything is working so fine")
        self.year = 30
    
    def eat(self):
        print("is eating")


class Mamal(Animal):
    def __init__(self):
        #override 
        super().__init__()
        print("mamal is working very well know")
        self.weight = 80


    def walk():
        print("we are mamal so we can walk")

m = Mamal()
print(m.year)
print(m.weight)