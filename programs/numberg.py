import random


random = random.randint(1,100)

while True:
    try:
        number_guess = int(input("Enter a number"))
        if number_guess < random:
            print("the number is too low")
        elif number_guess > random:
            print("The number is too high")
        else:
            print("YOU WIN!! Congratulation🙌🥳")
            break
    except ValueError:
        print("Enter a valid number please!! ")
