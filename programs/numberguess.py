import random
number_to_guess = random.randint(1,100)
while True:
    try:
        Guess = int(input("Enter the number between 1 to 100 "))
        if Guess < number_to_guess:
            print("Too Low")
        elif Guess > number_to_guess:
            print("Too High!")
        else:
            print("Congratulation You Guess")
            break
    except ValueError:
        print("Enter a valid number")



