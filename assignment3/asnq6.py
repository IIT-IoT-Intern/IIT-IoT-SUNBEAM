# -------- Arithmetic operation functions --------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b


# -------- Calculate function --------
def calculate(operand1, operand2, operation):
    return operation(operand1, operand2)


# -------- Testing calculate() with different inputs --------
num1 = int(input("Enter a 1st number: "))
num2 = int(input("Enter a 2nd number: "))
print("Addition:", calculate(num1, num2, add))
print("Subtraction:", calculate(num1,num2, subtract))
print("Multiplication:", calculate(num1,num2, multiply))
print("Division:", calculate(num1, num2, divide))

print("\nTesting with different values:")
print("for 5&6")
print("Addition:", calculate(5, 6, add))
print("Multiplication:", calculate(5, 6, multiply))
print("Division:", calculate(5, 6, divide))