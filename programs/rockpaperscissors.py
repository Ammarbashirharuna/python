import random
emojis = {'r': '🪨','s':'✂️','p':'📄'}
choice = ['r','p','s']
def user_choice():
    while True:
      user_choice = input("Rock Paper, Scissors ? (r/p/s) ")
      if user_choice in choice:
        return user_choice
    else:
         print("invalid choice!")

def displaying_choices(user_choice, computer_choice):
      print(f"You choose {emojis[user_choice]}")
      print(f"computer choose {emojis[computer_choice]}")
 

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif ((user_choice == 'r' and computer_choice == 's')
    or (user_choice == 's' and computer_choice == 'p')
    or (user_choice ==  'p'and computer_choice == 'r')):
       print("You win!")


def playing_game():
    while True:
       user_Choice = user_choice()

       computer_choice = random.choice(choice)
       displaying_choices(user_choice, computer_choice)
       determine_winner(user_choice, computer_choice)

       select_continue = input("Do you want to continue (Y/N) ").lower()
       if select_continue == 'n':
        break

playing_game()


