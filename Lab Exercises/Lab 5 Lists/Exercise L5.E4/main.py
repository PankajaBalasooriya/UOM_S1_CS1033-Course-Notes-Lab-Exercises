try:
    matrix = []
    while True:
        input_row = list(map(int, input().split()))
        if len(input_row) == 1 and -1 in input_row:
            break
        else:
            matrix.append(input_row)

    transpose = [[] for x in range(len(matrix[0]))]

    for k in range(len(matrix)):
        if len(matrix[k]) != len(matrix[k - 1]):
            matrix[len(matrix) + 1] = 0
    else:
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                transpose[i].append(matrix[j][i])


except ValueError:
    print("Error")
except IndexError:
    print("Invalid Matrix")
else:
    for i in range(len(transpose)):
        for j in range(len(transpose[0])):
            print(transpose[i][j], end=" ")
        print(end="\n")