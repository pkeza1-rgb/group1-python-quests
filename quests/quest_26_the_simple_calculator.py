#!/usr/bin/python3

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ").strip()
        
        if operation == "+":
            print("Result: {}".format(add(num1, num2)))
        elif operation == "-":
            print("Result: {}".format(subtract(num1, num2)))
        elif operation == "*":
            print("Result: {}".format(multiply(num1, num2)))
        elif operation == "/":
            print("Result: {}".format(divide(num1, num2)))
        else:
            print("Invalid operation selection.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    calculator()
