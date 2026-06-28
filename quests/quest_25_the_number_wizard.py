#!/usr/bin/python3
import random

def number_wizard():
    secret_number = random.randint(1, 100)
    print("Welcome to The Number Wizard!")
    print("I have chosen a secret number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the correct number.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    number_wizard()
