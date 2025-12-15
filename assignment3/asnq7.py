# Recursive function to find factorial
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n - 1)


# Recursive function to find power
def power(base, exp):
    if exp == 0:          # base case
        return 1
    else:
        return base * power(base, exp - 1)


# Testing the functions
num = int(input("Enter a number: "))
print("Factorial of", num, "=", factorial(num))

base = int(input("Enter a base: "))
exponent = int(input("Enter a exponent: "))
print(base, "power", exponent, "=", power(base, exponent))