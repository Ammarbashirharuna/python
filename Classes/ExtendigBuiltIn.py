class Text(str):
    def duplicate(self):
        return self + self

text = Text("PYTHON")
print(text.duplicate())
print(text.lower())

class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)

list = TrackableList()
list.append("2")
