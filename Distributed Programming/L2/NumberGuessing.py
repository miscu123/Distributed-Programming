import random

def number_guessing():
    n = random.randint(1, 20)
    guesses = 0
    while guesses < 5:
        guess = int(input("Guess a number between 1 and 20: "))
        if guess < n:
            print("Too low")
            guesses += 1
        elif guess > n:
            print("Too high")
            guesses += 1
        else:
            print("Correct")
            break

    print("The number was: ", n)


number_guessing()