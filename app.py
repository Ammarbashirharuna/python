from datetime import date
from math import ceil,floor
from re import split
# player1_health = 1200
# player2_health = 1100




#function
"""
def area_of_circle(r) :
    pi = 3.14
    area = pi * r * r
    return area

area = area_of_circle(20)
print(area)

#fstrings 
print(f"hello player {player1_health} it seems like you are the first player in this round");
#let's try something 
r = 30
print(area_of_circle(r))

#farameters of a function
def numbers(a,b):
    add = a + b
    return add
add = 50 + 30
print(add)

add = 200 + 500
print(add)
#varieble 
my_name = "ammar"
my_second_name = "bashir haruna"
name = my_name + " " + my_second_name
print(name)
def name(r):
    pi = 50
    area = pi * r * r
    return area
r = 50
print(name(r))
"""
# #function excercise
"""
def calculate_damage(damage_one,damage_2,damage_3):
    total = damage_one * damage_2 + damage_3
    return total
complete_damage = calculate_damage(50,50,50)
print(complete_damage)
"""
# #temprature
"""
def to_celcius(f):
    c = 5 / 9 * (f - 32)
    return c
converting = to_celcius(212)
print(converting)
"""
# #none return value
"""
def my_function():
   print( "i do something")
   return 

my_day = my_function()
"""

# #multiple return
"""
def my_player(first_name,last_name,power):
    power = power + 1 #we increase the power one
    title = f"{first_name}{last_name} the warrior" #we return the first name and last name of the warrior
    return title,power # we return multiple parameter with a diffrent value

my_day = my_player("ammar","bashir",100) #we have passed  the name of a player to the function as a parameter
print(my_day)
"""

# #scope
"""
def my_default():
    return modifier * level
modifier = 30
level = 20
print(my_default())
# name = input("enter your name?")
# print(f"Hello {name}")
# input("what is your namea")
# print("yusuf")
"""
# # list
"""
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list[0])
print(my_list[2])

print([1,2,3,] * 5)
x_list = []
y_list  = []
"""

# #string formating
"""
name = "ammar"
age = 20
print("my name is %s" %name)
print("my name is %s and i am %d  years old" %(name,age))
#string concatination
print("ammar" + "bashir" + "haruna")
"""
# #build in function to capitalize each word
"""
print("ammar".upper())
name = input("enter your name")
print("you are highly welcome",name)
"""
# #type of function
"""
x = input("enter your name")
print(type(x))
#reading interger from keyboard
"""
"""
x = int(input("enter first number"))
print(x)
x = 10
print("number is", str(x))
"""
#date and time
"""
date.today()
print(date.today())
#concatinating between  date and string
print("todays date is:", str(date.today()))
"""
#excercise from  microsoft 
"""
persecs = 11
lightyears = persecs * 3.68
print( str(persecs)  + "  is equibalent to :" + str(lightyears))
"""
#excercise to test my knowledge 
"""
persecs_input = input("Enter the number in persecs")
persecs = int(persecs_input)
lightyears = 3.2456 * persecs
print(persecs_input + "persecs is " + str(lightyears) + "light years")
"""
#if statement
"""
first = 50
second = 30
if first < second:
    print("the first number is greate than second");
else :
    print("NOpe you make a mistake bro")
"""
# elif statement 
a = 60 
b = 4
if a < b :
    print("a is lesthan b")
elif a >= b :
    print("it seems like they are thesame")
else :
    print("oops i dont know")
#nested if 
a = 80
b = 40
c = 20
if a < b:
    if a < c:
        print("a is greater than all")
elif a > b:
    print("it seems like a is the biggest")

else:
    print("i dont know the reality")
#and and or operator
a = 34
b = 50
if a == 34 or  b == 34 :
    print(a + b)
else:
    print("opps i cant do that because i did not found anything similar")
#string
fact = "it seems like you can not make this happen in this morning so to tacle this that is why"
print(fact)
time = 'the near site to the "system" is so close to our work station so that is why am just leave the space'
print(time)
time = """this is what are deserve to use: am not here. this is time"""
print(time)
#string method practice
string_method = "today is monday and i started learning python so its cool".title()
print(string_method)
#using variable settings
me = "am python developer"
to = me.title()
print(to)

#split method 
my_day = "i am really hurt about some time because am not familiar with it: 2030 i will".split()
print(my_day)
#search for a string
my_words =  "am" in "Hello guys am sorry for not being there so am really trying to update my time from today to perfom"
print(my_words)
#practice
time_search = "Assalamu" in "Assalamu alaikum guys welcome to our startup company hope you are doing well"
print(time_search)
#find mesthod searching for a string
me = """you are really welcome to our project and we hope you can achieve anything we assign you to do"""
print(me.find("to"))
#a way to count  for a string is using count method to find how many times it appears
temprature = "hello guys our time it has more convienient time here so please do what is taking us for here"
print(temprature.count("time"))
#check content in python
temprature = "the mars temprature is: 50% C and the marcury is"
part = temprature.split(':')
print(part)
print(part[-1])
#using irregular method
temprature = "the reason why temprature is 50 % 80 C in nothan is that "
for item in temprature.split():
    if item.isnumeric():
        print(item)
#practice
time  = "hello guys how are you doing hope you are doing well so know its exactly 50 years from our meeting 47"
for item in time.split():
    if item.isnumeric():
        print(item)
print("saturn has a daytime of -35 degree celcius and marcury has 40 % celcius ".replace("celcius","C"))
#using .join method to join every item in the list
list = "the are alot of problem that we are facing, there in nigeria but no one care about them"
print(''.join(list))
temprature = "lorem30 an not reay sure tomorrow temprature it can be good for our health and other days temprature is more high"
#string formating using % sign formating using multiple values
print("""i really dont know what is going in my %s because am seeing like %s is not serious""" % ("town","all"))
#using single values
print("""today is not %d time""" %12)
#ANOther banger
print("Hello guys today is my birthday am %d" %50)
#using format method
numbers = "1/8"
print("we rally need our time to {} make something".format(numbers))
#using assign variables 
marse = 30/2
print("""you know sometime i dont know that {0} is the most beutifull town in the world {1} so am really happy {0} """.format("kano",marse))
#make it more readable when using carly braces
marse = 30/2
print("""you know sometime i dont know that {kano} is the most beutifull town in the world {marse} so am really happy {kano} """.format(kano="kano",marse=marse))
#string formating using format method 
my_name = "ammar".upper()
print("hello guys my name is {my_name} and i am also the founder of this place {my_name}".format(my_name=my_name))
#floor division to convert seconds to a minute
seconds = 1024
seconds_to_minute = 1024 // 60
print(seconds_to_minute)
seconds  = 1042
to_minute = 1042 // 60
to_reminder = 1042 % 60
print(to_reminder)
#order of operation 
result_of = 1030 + (3 * 4)
print(result_of)
#converting to string 
to_inr = int("2345")
print(to_inr)
#absolute debiation to print the absolute of a number because how you enter the number is not matter
print(abs(24 - 20))
print(abs(20 - 24))
#rounding to print the round of a number to the nearest integer  if the decimal is nearest to  .5 or lessthan .5
print(round(1.5))
print(round(3.9))
print(round(2.5))
#using math linbrary to round the numbers to down  or up 
time = ceil(12.5)
print(time)
rounding = floor(13.6)
print(rounding)
#list (new module)
list = ["mercury","earch","mars","jupiter","neptune","pluto"]
print("the first planet is ",list[0])
print("the third planet is ",list[1])
print("the second planet is ",list[2])
list[3] = "pluto"
print(list[3])
#using len() function to calculate the number of planet in the list
planet = ["marcury","venus","earth","mars","jupyter"]
number_of_planet = len(planet)
print("the number of planet in the surface is",number_of_planet,"in the surface")
#practice
numeric = ["time","movement","distructuring","marcury"]
print(len(numeric))
print(numeric[3])
numeric.append("my movement")
print(numeric)
numeric
#list
list = ["ammar","dauda","faizu","abubakar","ibrahim","abdul"]
print(list)
#changing the index  name in the list
list [2] = "yaya faizu"
print(list)
list[1] = "yaya dauda"
print(list)
#adding value to the list
list.append("aminu")
list.append("musa")
list.append("abdurrahman")
list.append("idris")
#removing value to the list
list.pop()
list.pop()
list.pop()
print(list)
#determinig the length of a list
number_of_item =  len(list)
print(number_of_item)
#printing negative index in a list
index =  list[-1]
print(index)
#serching item in the list to do so we have to  use index
index_of_yaya = list.index("yaya dauda")
print(index_of_yaya)
#loops
#while lopps
i = 1
while i < 10:
    print("may be not today", i)
    i = i + 1
print("it works")
i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
print("terminate")
Astron
canva






