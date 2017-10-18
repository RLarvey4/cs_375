
import random

def main():
    print("I'm thinking of a number between 1 and 100, can you guess it?")

    magic_number = random.randrange(1, 101)
    guess = 0
    attempts = 1

    while guess != magic_number:
        guess = eval(input("what is your guess?"))

        if guess < magic_number :
            print("you are too low!")

        elif guess > magic_number :
            print("you are too high!")

        else:
            print("you got it! It took you", attempts, "tries.")

        attempts = attempts + 1

main()

