# Function to calculate the average per column of a tuple of tuples
def average_tuple_of_tuples(data):
    # zip(*data) groups elements from each inner tuple by column
    # sum(x) / len(x) computes average of each group
    averages = [sum(col) / len(col) for col in zip(*data)]
    return averages

# Given tuple of tuples
input_data = ((10, 10, 10, 12),
              (30, 45, 56, 45),
              (81, 80, 39, 32),
              (1, 2, 3, 4))

# Calculate averages
result = average_tuple_of_tuples(input_data)

# Print the result
print(result)
