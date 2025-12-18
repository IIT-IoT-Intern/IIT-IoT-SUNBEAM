# main.py

import calculator  # import our module

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
print("Addition:", calculator.add(num1, num2))
print("Subtraction:", calculator.subtract(num1, num2))
print("Multiplication:", calculator.multiply(num1, num2))
print("Division:", calculator.divide(num1, num2))
