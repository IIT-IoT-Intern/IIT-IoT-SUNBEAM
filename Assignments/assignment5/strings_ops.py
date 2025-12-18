# string_ops.py

def reverse_string(s):
    """Return the reversed version of the string."""
    return s[::-1]  # slicing method reverses the string

def count_vowels(s):
    """Return the number of vowels in the string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
