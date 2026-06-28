#!/usr/bin/python3

def code_breaker():
    secret_code = "42"
    attempts = 3
    
    print("Welcome Agent. You have 3 attempts to break the secret code.")
    
    for attempt in range(1, attempts + 1):
        guess = input("Attempt {}/3 - Enter code: ".format(attempt)).strip()
        
        if guess == secret_code:
            print("Access Granted. Code broken successfully!")
            return
        else:
            if attempt < attempts:
                print("Incorrect code. Try again.")
            else:
                print("Access Denied. Out of attempts.")

if __name__ == "__main__":
    code_breaker()
