while True:
    n = int(input())

    is_Prime = False

    if n < 0:
        break
    else:
        if n == 1:
            is_Prime = False
        elif n == 2:
            is_Prime = True
        else:
            for i in range(2, n, 1):
                if n % i == 0:
                    is_Prime = False
                else:
                    is_Prime = True
                if not is_Prime:
                    break

        if is_Prime:
            print("prime")
        else:
            print("non-prime")
