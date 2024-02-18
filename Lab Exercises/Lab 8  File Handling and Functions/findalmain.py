def getNum():
    """Reads a number from a text file given by the user and returns the valid number read from the file or None if the
    input is invalid
    """
    # Read the input file name from the user
    input_file_name = input()

    # Open the input file for reading
    with open(input_file_name, "r") as input_file:
        # Iterate over each line in the file and read
        for line in input_file:
            number = line

    try:
        # Convert the read line to an integer
        number = int(number)
    except ValueError:
        # Return None for an invalid input
        return

    # Check if the number is between 0 and 20 and return valid number
    if 0 <= number <= 20:
        return number
    else:
        return


def show(n, result):
    """Prints the Fibonacci sequence and returns the formatted string representation of the Fibonacci number"""
    # Creating formatted string
    print_command = f"Fibonacci({n}) = {result}"
    print(print_command)
    return print_command


def saveFile(write_text):
    """Saves the text to a file"""
    with open("result.txt", "w") as output_file:  # Open the output file in write mode
        output_file.write(write_text)  # Write to the file
    return


def generateFibonacci(num):
    """
    Generates the Fibonacci sequence for a given number using iteration and incrementation and Returns the Fibonacci
    number corresponding to the input number.
    """
    if num == 0:
        return 0
    if num == 1:
        return 1

    a = 0
    b = 1
    fibNum = 1
    for i in range(2, num + 1):
        fibNum = a + b
        a = b
        b = fibNum
    return fibNum


# Call the getNum() function
n = getNum()

# Check if a valid number was obtained
if n is not None:
    # Get the Fibonacci number corresponding to n
    fibonacciNumber = generateFibonacci(n)

    # Show the Fibonacci number and save it to a file
    saveFile(show(n, fibonacciNumber))
else:
    # print invalid for incompatible values
    print("Invalid input!")
