import time

def add_numbers(a, b):
    try:
        a = float(a)
        b = float(b)
        return a + b
    except ValueError:
        return "Invalid input. Please enter numeric values."

def subtract_numbers(a, b):
    try:
        a = float(a)
        b = float(b)
        return a - b
    except ValueError:
        return "Invalid input. Please enter numeric values."

def mutiply_numbers(a, b):
    try:
        a = float(a)
        b = float(b)
        return a * b
    except ValueError:
        return "Invalid input. Please enter numeric values."
    
def divide_numbers(a, b):
    try:
        a = float(a)
        b = float(b)
        return a / b
    except ValueError:
        return "Invalid input. Please enter numeric values."
    except ZeroDivisionError:
        return "Cannot divide by zero."

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
opration = input("Enter operation (add +, subtract -, multiply *, divide /): ").strip().lower()

if opration == "add" or "+":
    time.sleep(1)
    print(add_numbers(num1, num2))
elif opration == "subtract" or "-":
    time.sleep(1)
    print(subtract_numbers(num1, num2))
elif opration == "multiply" or "*":
    time.sleep(1)
    print(mutiply_numbers(num1, num2))
elif opration == "divide" or "/":
    time.sleep(1)
    print(divide_numbers(num1, num2))
else:
    time.sleep(1)
    print("Invalid operation. Please enter add, subtract, multiply, or divide.")

