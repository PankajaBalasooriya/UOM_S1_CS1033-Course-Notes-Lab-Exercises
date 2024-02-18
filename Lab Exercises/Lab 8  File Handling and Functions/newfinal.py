def getNum():
    """Reads a number from a text file given by the user

    Returns the valid number read from the file or None if the input is invalid
    """
    # Read the input file name from the user
    input_file_name = input()

    # Open the input file for reading
    with open(input_file_name, "r") as input_file:
        # Iterate over each line in the file
        for line in input_file:
            number = int(line)

    # Check if the number is between 0 and 20 and return valid number
    if 0 <= number <= 20:
        return number
    else:
        # Print an error message for invalid input
        print("Invalid input!")
        return  # Return None if the input is invalid


def show(n, result):
    """Prints the Fibonacci sequence

    Args
        n  The input number
        result  The Fibonacci sequence corresponding to the input number

    Returns the formatted string representation of the Fibonacci sequence
    """
    # Creating formatted string
    print_command = f"Fibonacci({n}) = {result}"
    print(print_command)
    return print_command


def saveFile(write_command):
    """Saves the command to a file

    Args
        write_command  The Text to be written to the text document
    """
    with open("result.txt", "w") as output_file:    # Open the output file in write mode
        output_file.write(write_command)    # Write to the file
    return


def generateFibonacci(num):
    """Generates the Fibonacci sequence for a given number

    Args
        num  The input number

    Returns the Fibonacci sequence corresponding to the input number
    """
    if num == 0:    # Base case Fibonacci(0) = 0
        return 0
    if num == 1:    # Base case Fibonacci(1) = 1
        return 1
    # Using recursion to generate the Fibonacci sequence
    fibonacciSequence = generateFibonacci(num - 1) + generateFibonacci(num - 2)
    return fibonacciSequence


# Call the getNum() function
n = getNum()

# Check if a valid number was obtained
if n is not None:
    # Generate the Fibonacci sequence
    fibSeq = generateFibonacci(n)

    # Show the Fibonacci sequence and save it to a file
    saveFile(show(n, fibSeq))
