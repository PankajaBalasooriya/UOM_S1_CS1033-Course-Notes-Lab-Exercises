def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    number = int(input("Enter a positive integer (or a negative integer to terminate): "))
    if number < 0:
        break
    if is_prime(number):
        print(number, "is prime.")
    else:
        print(number, "is not prime.")
