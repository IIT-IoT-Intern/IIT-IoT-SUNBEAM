# Program to accept two numbers and display division
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the second number is zero before dividing
if num2 == 0:
    print("Error: Cannot divide by zero!")
else:
    result = num1 / num2
    print("Result of division:", result)
