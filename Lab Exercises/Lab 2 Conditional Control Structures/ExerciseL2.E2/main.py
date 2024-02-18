date = input()

y = int(date[0:4])
m = int(date[5:6])
d = int(date[7:9])

if m < 3:
    m = m + 12
    y = y - 1
a = (2 * m) + 6 * (m + 1) // 10
b = y + (y // 4) - (y // 100) + (y // 400)
f1 = d + a + b + 1
f = round(f1 % 7)
print(f)
