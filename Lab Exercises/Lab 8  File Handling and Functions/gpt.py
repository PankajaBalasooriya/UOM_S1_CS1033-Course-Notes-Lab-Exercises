def getNum():
    """Reads a number from a text file specified by the user"""
    # Read the input file name from the user
    input_file_name = input()  # Prompt the user to enter the input file name

    # Open the input file for reading
    with open(input_file_name, "r") as input_file:  # Open the specified file in read mode
        for line in input_file:  # Iterate over each line in the file
            number = int(line)  # Convert the line to an integer

    if 0 <= number <= 20:  # Check if the number is between 0 and 20 (inclusive)
        return number  # Return the valid number
    else:
        print("Invalid input!")  # Print an error message for invalid input
        return  # Return None if the input is invalid


def show(n, result):
    print_command = f"Fibonacci({n}) = {result}"  # Create a formatted string with Fibonacci sequence information
    print(print_command)  # Print the formatted string
    return print_command  # Return the formatted string


def saveFile(write_command):
    with open("result.txt", "w") as output_file:  # Open/create the output file in write mode
        output_file.write(write_command)  # Write the given command to the file
    return


def generateFibonacci(num):
    if num == 0:  # Base case: Fibonacci(0) is 0
        return 0
    if num == 1:  # Base case: Fibonacci(1) is 1
        return 1
    fibonacciSequence = generateFibonacci(num - 1) + generateFibonacci(
        num - 2)  # Recursive call to generate the Fibonacci sequence
    return fibonacciSequence  # Return the calculated Fibonacci sequence for the given number


n = getNum()  # Call the getNum() function to get a valid number from the user
if n is not None:  # Check if a valid number was obtained
    fibSeq = generateFibonacci(n)  # Generate the Fibonacci sequence for the given number
    saveFile(show(n, fibSeq))  # Show the Fibonacci sequence and save it to a file