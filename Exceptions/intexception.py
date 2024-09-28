
try:
     number = int(input("Enter some number"))
     print(number)
except ValueError:
        print("please enter a number not some words")
age = 30
try:
    while True:
         welcome = int(input("Enter your age "))
         if welcome == age:
            print("Welcome sir")
         else:
            print("Am sorry you are not")
except ValueError:
    print("Enter a valid age please")