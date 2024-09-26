import random 
while True:
    roll = input("Do you want roll the dice(Y/N)? ")
    if roll == 'Y':
         random1 = random.randint(1,6)
         random2 = random.randint(1,6)
         print(f'({random1}, {random2})')
         break
    if roll == 'N':
        print("Thanks for playing")
        break
    else:
        print("invalid input please select the right answer")

my_name = ""
names = []
my_name = input("enter your name please")
print(f"Hello {my_name} Do your wnt add some names to your name lists?  ")
adding_names = input("(Y/N) ").lower()
if adding_names = 'Y':
   while True:
    print("Entrt names ")
    names.append(adding_names)
    if adding_names == "Done":
        print(f"you have added {}")
if adding_names = 'N':
    print("okay you are highly welcome sir goodbye !")
    break 
print(" am happy to have you onboard sir hope to be with you and i hope anything will be fine soon because currently we are trying to make evrything ready by tomorow so hope to see you there on board")