first_name = input("Your name please  ")
search = "a" in first_name
if search == True:
    print("your are eligible to go for another step")
    second_name = input("your second name")
    search = "m" in second_name
    if search == False:
        print("You are good to go ")
    else:
        print("your name is not eligible for know")
else:
    print("sorry")
#short circuit
is_boy = True
a_student = False
if (is_boy and a_student) or (is_boy and not a_student):
    print("hmmm you are eligible boy")
    


