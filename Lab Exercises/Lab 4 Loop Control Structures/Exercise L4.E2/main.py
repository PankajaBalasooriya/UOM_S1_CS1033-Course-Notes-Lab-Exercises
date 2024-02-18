number = int(input("Input number: "))

if number < 2:
    print("Invalid Input")
else:
    number_of_abundant_numbers = 0
    for k in range(2, number + 1):
        sum = 0
        for i in range(1, k):
            if k % i == 0:
                sum += i
        if sum > k:
            number_of_abundant_numbers += 1
    print(f"Number of abundant numbers from 1 to {number} is {number_of_abundant_numbers}")