# prompting the user to enter 10 numbers
input_numbers = input()

# split the input into a list of numbers
numbers = input_numbers.split()

# convert the list of numbers from strings to floats using map function
numbers_float = list(map(float, numbers))

# finding the maximum and minimum values in the list of floats
maximum_value = max(numbers_float)
minimum_value = min(numbers_float)

# finding the index of the maximum and minimum values in the list
max_index = numbers_float.index(maximum_value)
min_index = numbers_float.index(minimum_value)

# display the minimum and maximum values in the list
print(f'Minimum = {numbers[min_index]}')
print(f'Maximum = {numbers[max_index]}')
