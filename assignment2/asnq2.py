# Program to check whether a 5-digit number is a numeric palindrome

num = int(input("Enter a 5-digit number: "))

original_num = num

reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

if original_num == reversed_num:
    print(f"{original_num} is a palindrome number.")
else:
    print(f"{original_num} is not a palindrome number.")
