from abc import ABC, abstractmethod

"""
in duck typing we dont necessaraly define a class UIcontrols that other classes need to inherit from
 what we only have to make sure is that we pass
a draw method to every class in a polymophism
"""


class RadioButon:
    def draw(self):
        print("Am radio button")

class SubmitButon:
    def draw(self):
        print("Submit me please")

class FormInput:
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