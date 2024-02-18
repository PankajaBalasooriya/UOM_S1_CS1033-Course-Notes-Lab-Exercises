while True:
    n = int(input())

    if n < 0:
        break

    sqrt = int(n ** (1 / 2))

    if n == 1 or n == 0:
        print("non-prime")
    else:
        for i in range(2, sqrt + 1, 1):
            if n % i == 0:
                print("non-prime")
                break
        else:
            print("prime")