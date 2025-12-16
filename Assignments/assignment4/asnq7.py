# Creating a 3x4 matrix as list of lists
matrix_list = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [20, 30, 40, 50]
]

# Creating another 3x4 matrix as tuple of tuples
matrix_tuple = (
    (5, 10, 15, 20),
    (10, 15, 20, 25),
    (15, 20, 25, 30)
)

# Function to add & subtract two matrices
def add_and_subtract(mat1, mat2):
    # Result matrices as lists (mutable)
    add_result = []
    sub_result = []

    # Loop through rows by index
    for i in range(len(mat1)):
        # Calculate row additions/subtractions
        add_row = []
        sub_row = []
        for j in range(len(mat1[0])):
            add_row.append(mat1[i][j] + mat2[i][j])
            sub_row.append(mat1[i][j] - mat2[i][j])

        add_result.append(add_row)
        sub_result.append(sub_row)

    return add_result, sub_result

# Main block
addition_matrix, subtraction_matrix = add_and_subtract(matrix_list, matrix_tuple)

print("Addition of matrices:")
for row in addition_matrix:
    print(row)

print("\nSubtraction of matrices:")
for row in subtraction_matrix:
    print(row)
