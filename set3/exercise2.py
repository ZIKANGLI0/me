"""Set 3, Exercise 2.

An example of how a guessing game might be written.
Play it through a few times, but also stress test it. What if your lower bound 
is 🍟, or your guess is "pencil", or "seven"
This will give you some intuition about how to make exercise 3 more robust.
"""


import random

def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nWelcome to the guessing game!")
    print("A number between 0 and _ ?")
    
    while True:
        try:
            upperBound = input("Enter an upper bound: ")
            upperBound = int(upperBound)
            if upperBound <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    print(f"OK then, a number between 0 and {upperBound} ?")
    actualNumber = random.randint(0, upperBound)

    guessed = False

    while not guessed:
        try:
            guessedNumber = input("Guess a number: ")
            guessedNumber = int(guessedNumber)
            print(f"You guessed {guessedNumber},")
            if guessedNumber == actualNumber:
                print(f"You got it!! It was {actualNumber}")
                guessed = True
            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    return "You got it!"

if __name__ == "__main__":
    exampleGuessingGame()