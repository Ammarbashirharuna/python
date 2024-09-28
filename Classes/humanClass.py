class Human:
    #class attribute
    default_skin_color = "black"
    def __init__(self, eat, drink):
            self.eat = eat
            self.drink = drink



    def walk(self):
        print(f"{self.eat}, {self.drink} yeah you are human")

human = Human("i","g")
see = human.walk()
#another human
men = Human("i have black hair", "i am tall")
men.walk()
print(Human.default_skin_color)
print(men.default_skin_color)

