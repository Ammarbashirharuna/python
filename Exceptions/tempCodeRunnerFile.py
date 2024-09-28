try:
    #opening a file
    with open("app.py") as file:
        print("file open..")
    age = int(input("Age "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) :
    print("you have enterd invalid age please check")
else:
    print("Welldone sir")