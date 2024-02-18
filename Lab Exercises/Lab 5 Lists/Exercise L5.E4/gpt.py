matrix = []
while True:
    try:
        input_row = list(map(int, input().split()))
    except ValueError:
        print("Error")
    if len(input_row) == 1 and -1 in input_row:
        break
    else:
        matrix.append(input_row)

transpose = [[] for x in range(len(matrix[0]))]

try:
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            transpose[i].append(matrix[j][i])
except IndexError:
    print("Invalid Matrix")
else:
    for i in range(len(transpose)):
        for j in range(len(transpose[0])):
            print(transpose[i][j], end=" ")
        print(end="\n")
