def input_matrix(rows, cols):
    """Read in the elements of the matrix of given order"""
    try:
        matrix = []
        for i in range(rows):
            # Read input for each row and convert it to a list of integers
            row_input = list(map(int, input().split()))
            matrix.append(row_input)

        # Check if each row has the expected number of columns
        for j in range(rows):
            if len(matrix[j]) != cols:
                print("Invalid Matrix")
                return None
        # Return the matrix if it is valid
        return matrix
    except Exception :
        print("Error")
        return None


def transpose(matrix):
    """Calculate the transpose of a matrix"""
    transposed_matrix = [[] for i in range(len(matrix[0]))] # Create an empty transposed matrix
    for row in matrix:
        for index in range(len(row)):
            # Swap rows and columns to get the transpose
            transposed_matrix[index].append(row[index])
    return transposed_matrix


def product_of_matrices(matrix1, matrix2):
    """Calculating product of two matrices given and returning the product matrix"""
    product_matrix = [[[] for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for k in range(len(matrix2[0])):
            total_sum = 0
            for j in range(len(matrix2)):
                # Multiply corresponding elements and accumulate the sum
                product = matrix1[i][j] * matrix2[j][k]
                total_sum += product
            # Assign the sum to the corresponding cell in the product matrix
            product_matrix[i][k]= total_sum
    return product_matrix


def print_matrix(matrix):
    """Printing the the given matrix"""
    for row in matrix:
        for num in row:
            # Print each element followed by a space
            print(num, end=" ")
        # Print a new line after each row
        print("")


dimensions = list(map(int, input("Enter the dimension: ").split(",")))

# Read and store Matrix A
print("Enter Matrix A: ")
matrix_a = input_matrix(dimensions[0], dimensions[1])

if matrix_a is not None:
    # Read and store Matrix B
    print("Enter Matrix B: ")
    matrix_b = input_matrix(dimensions[0], dimensions[1])
    if matrix_b is not None:
        # Transpose Matrix B
        matrix_b = transpose(matrix_b)
        # Calculate the product of Matrix A and Transposed Matrix B and print the product matrix
        print_matrix(product_of_matrices(matrix_a, matrix_b))