import random
words = ["ticket", "market", "Apple", "coffee", "clock"]
randomwords = random.choice(words)
guesstime = 0
guesslimit = 3
while guesstime <= guesslimit:
    try:
        if guesstime == guesslimit:
            break
        guess = str(input("Guess the secret word "))
        if guess not in randomwords:
            print("Sorry guess again ")
        elif guess in randomwords:
            print("You Win!! 🥳🥳👾")
            break
    except ValueError:
        print("Sorry Enter a word not a letter please!!")
