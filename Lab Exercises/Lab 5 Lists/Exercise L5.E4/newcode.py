# Using exception handling to catch Errors in the code
try:
    matrix = []
    # Take input for the matrix until -1 is entered
    while True:
        input_row = list(map(int, input().split()))
        if len(input_row) == 1 and -1 in input_row:
            break
        else:
            matrix.append(input_row)
    # Create an empty matrix for the transpose
    transpose = [[] for x in range(len(matrix[0]))]

    # Check if the current row has a different length than the previous row
    for k in range(len(matrix)):
        length = len(matrix[0])
        if len(matrix[k]) != len(matrix[k - 1]):
            length += 1
    else:
        # Add elements to the transpose matrix
        for i in range(length):
            for j in range(len(matrix)):
                transpose[i].append(matrix[j][i])

except Exception as ex:
    # Checking the type of exception and giving the required output for the exceptions
    if type(ex) == IndexError:
        print("Invalid Matrix")
    else:
        print("Error")
else:
    # If no exceptions arise print the transpose matrix
    for i in range(len(transpose)):
        for j in range(len(transpose[0])):
            print(transpose[i][j], end=" ")
        print(end="\n")
