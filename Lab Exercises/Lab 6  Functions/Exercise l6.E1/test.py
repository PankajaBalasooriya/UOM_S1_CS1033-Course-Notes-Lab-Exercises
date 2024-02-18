matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix2 = [[4, 5, 6], [7, 8, 9], [10, 11, 12],[13, 14, 15]]

'''
prdmtrx = [[[] for p in range(len(matrix2[0]))] for q in range(len(matrix1))]
for i in range(len(matrix1)):
    for k in range(len(matrix2[0])):
        for j in range(len(matrix2)):
            a = matrix1[i][j]
            b = matrix2[j][k]
'''

def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print("")

print_matrix(matrix1)

'''
prdmtrx = [[[] for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
print(prdmtrx)
'''