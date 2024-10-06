from abc import ABC, abstractmethod

class UIControl(ABC):
    def draw(self):
        pass

class RadioButon(UIControl):
    def draw(self):
        print("Am radio button")

class SubmitButon(UIControl):
    def draw(self):
        print("Submit me please")

class FormInput(UIControl):
    def draw(self):
        print("input here")

class Click:
    def draw(self):
        print("click here to continue")

def draw(controls):
    for control in controls:
        control.draw()

rb = RadioButon()
sb = SubmitButon()
fi = FormInput()
cl = Click()
draw([rb,sb,fi,cl])