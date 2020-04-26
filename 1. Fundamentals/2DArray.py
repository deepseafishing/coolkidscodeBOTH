# Initializing 2D array
N = 3
# This will Not work because the list is pass by reference. Each element will refer to the same list.
wrong_matrix = [[0 for i in range(0, N)]] * N
wrong_matrix[0][1] = 1
print(wrong_matrix)

# This is how you can initialize a 2D array.
right_matrix = [[0 for i in range(0, N)] for J in range(0, N)]
right_matrix[0][1] = 1
print(right_matrix)
