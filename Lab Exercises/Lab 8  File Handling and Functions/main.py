def getNum():
    """Reads a number from a text file specified by the user"""
    # Read the input file name from the user
    input_file_name = input()

    # Open the input file for reading
    with open(input_file_name, "r") as input_file:
        for line in input_file:
            number = int(line)

    if 0 <= number <= 20:
        return number
    else:
        print("Invalid input!")
        return


def show(n, result):
    
    print_command = f"Fibonacci({n}) = {result}"
    print(print_command)
    return print_command


def saveFile(write_command):
    with open("result.txt", "w") as output_file:
        output_file.write(write_command)
    return


def generateFibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    fibonacciSequence = generateFibonacci(num - 1) + generateFibonacci(num - 2)
    return fibonacciSequence


n = getNum()
if n is not None:
    fibSeq = generateFibonacci(n)
    saveFile(show(n, fibSeq))
