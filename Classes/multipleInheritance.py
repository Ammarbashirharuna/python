class Employee:
    def greet(self):
        print("good morning sir")


class Parson:
    def said(self):
        print("how you sir")


class Manager(Employee, Parson):
    pass

manager = Manager()
manager.greet()