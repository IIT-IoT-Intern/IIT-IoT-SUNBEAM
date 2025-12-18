# calculator.py
import calculator 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
# main.py

# import our module

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
print("Addition:", calculator.add(num1, num2))
print("Subtraction:", calculator.subtract(num1, num2))
print("Multiplication:", calculator.multiply(num1, num2))
print("Division:", calculator.divide(num1, num2))
