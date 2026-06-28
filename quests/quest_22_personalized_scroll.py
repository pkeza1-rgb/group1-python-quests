# Quest 22: The Personalized Scroll
# Concept: Functions with parameters - the function acts on data we give it.

def personalized_greeting(name, quest):
    print(f"Greetings, {name}! Your quest today is: {quest}.")

# Get the info from the user first
user_name = input("What is your name, adventurer? ")
user_quest = input("What quest do you seek? ")

# Pass the answers in as arguments
personalized_greeting(user_name, user_quest)
