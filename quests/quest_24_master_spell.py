# Quest 24: The Master Spell
# Concept: Calling a function from within another, or passing one
# function's result into another - breaking a big problem into small parts.

def ask_for_age():
    age = int(input("How many years have you walked this earth? "))
    return age

def can_they_vote(age):
    if age >= 18:
        print("You are old enough to vote!")
    else:
        print("Sorry, you must wait a few more years to vote.")

# First, get the age (function #1's job)
user_age = ask_for_age()

# Then, pass that result into function #2
can_they_vote(user_age)
