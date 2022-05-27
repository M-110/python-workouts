"""
Write a function (guessing_game) that takes no arguments.

When run, the function chooses a random integer between 0 and 100 (inclusive).

Then ask the user to guess what number has been chosen.

Each time the user enters a guess, the program indicates one of the following:

Too high

Too low

Just right

If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.

The program only exits after the user guesses correctly.
"""

from random import randint

def guessing_game():
    print('Welcome to the guessing game version 1')
    answer = randint(0,100)
    while (guess := int(input("Guess a number: "))) != answer:
        if guess < answer:
            print('Too low')
        else:
            print('Too high')
    print("Just right!")


# With input error handling:
    
def guessing_game2():
    print('Welcome to the guessing game version 2')
    answer = randint(0,100)
    while True:
        try:
            guess = int(input("Guess a number: "))
        except ValueError:
            print('Please enter a valid number')
            continue
        
        if guess < answer:
            print('Too low')
        elif guess > answer:
            print('Too high')
        else:
            print("Just right!")
            break
    
guessing_game()

guessing_game2()