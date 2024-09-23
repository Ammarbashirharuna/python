#without exception handling
# age = int(input("Age "))
# print("age")
#with exception
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

