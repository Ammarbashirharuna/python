#this is a parent or Base. because its where child will inherit
class Animal:
    def __init__(self):
        self.age = 20
    def eat(self):
        print("eat")

#this is a child or sub it inherit from a parent
class Mamal(Animal):
    def walk(self):
        print("walking")
#also a child base
class fish(Animal):
    
    def swiming():
        print("swin")
#checking for what they have inherit from animal
m = Mamal()
m.eat()
print(m.age)
