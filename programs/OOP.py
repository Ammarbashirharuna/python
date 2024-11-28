class speaker:
    brand = "sound"
    def __init__(self,color,model):
        self.color = color #instance attribut
        self.model = model # instance attribute



    def poweron(self): #instance methods
        print("powring on the speaker")
        print(f"the speaker is {self.color} and the model is {self.model}")
    
    def poweroff(self):
        print("powering off the speaker")



first_speaker = speaker("black", "Ex56")
print(first_speaker.color)
print(first_speaker.model)
print(first_speaker.brand)
print(first_speaker.poweron())