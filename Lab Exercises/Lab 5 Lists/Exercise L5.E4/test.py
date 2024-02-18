# lb 5 q3

for i in range(0, 4):
    marks = input().split()

list_of_marks = list(marks)

total = 0
for j in range(0, 4):
    for k in range(0, 3):
        total = total + int(list_of_marks[i][j])
        average = total / 3

    print('total=', total)
    print('average=', round(average, 1))



