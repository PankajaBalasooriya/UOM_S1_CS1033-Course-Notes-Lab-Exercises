p = []
inputs = []
while True:
    row_input = str(input())
    if row_input == '-1':
        break
    l = row_input.split('\n')

    inputs.append(l)

for i in inputs:
    try:
        n = [int(x) for x in i[0].split()]
    except:
        p = []
        print('Error')
        break

    if len(p) > 0:
        if len(p[0]) == len(n):
            p.append(n)
        else:
            p = []
            print('Invalid Matrix')
            break
    else:
        p.append(n)

if len(p) > 0:
    for k in range(len(p[0])):
        y = ''
        for j in range(len(p)):
            y = y + str(p[j][k]) + ' '
        print(y)
