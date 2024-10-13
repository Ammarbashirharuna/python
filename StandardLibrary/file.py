import os
fruits = ["apple", "banana","pineapple", "mango", "guava", "cheaps", "cashue", "milk", "guav"]
#opening file and write some data into it
filename = "fuit.txt"
with open(filename, 'w') as file:
    for fruit in fruits:
        file.write(fruit + "\n")
#reading data from file
with open(filename, 'r') as file:
    for fruit in fruits:
        print(fruit)

#appending data to a file
with open(filename, 'a') as file:
    for fruit in fruits:
        file.write(fruit + "\n")
    
    print("append successifully")

#deleting file
if os.path.exists("mytext.txt"):
    os.remove("mytext.txt")
    print("file deleted successfully sir!")
else:
    print("this file does not exists")
