from customtkinter import *
app =  CTK()
app.geometry("500x400")
btn = CTK.Button(master=app,text="clickme")
btn.place(relx=0.5,rely=0.5,anchor="center")
app.mainloop()