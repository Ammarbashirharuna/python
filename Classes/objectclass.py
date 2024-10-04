class Animal:
    def __init__(self):
        self.year = 30
    
    def eat(self):
        print("is eating")


class Mamal(Animal):
    def walk():
        print("we are mamal so we can walk")

m = Mamal()
m.eat()
print(isinstance(m,Animal))
#subclass
print(issubclass(Mamal,Animal))