import tkinter as tk
window = tk.Tk()
window.title("My first GUI")
label = tk.Label(window, text="Enter you name")
label.pack()
entry = tk.Entry(window)
entry.pack()
#age entry
label = tk.Label(window, text="Enter your Age")
label.pack()
entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="submit")
button.pack()
def submit():
    name = entry.get()
    age = entry.get()
    label["text"] = f"Hello, {name}!"
    label["text"] = f"your age is, {age} enjoy your day"
button.config(command = submit)

window.mainloop()