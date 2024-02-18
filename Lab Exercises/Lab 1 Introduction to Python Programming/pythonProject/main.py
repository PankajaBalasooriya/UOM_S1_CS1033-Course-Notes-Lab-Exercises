def float_to_binary(float_num):
    binary_num = ""

    # Extract the sign bit
    if float_num < 0:
        binary_num += "1"
        float_num = abs(float_num)
    else:
        binary_num += "0"

    # Extract the integer and fractional parts separately
    integer_part = int(float_num)
    fractional_part = float_num - integer_part

    # Convert the integer part to binary
    binary_num += bin(integer_part)[2:].zfill(1)

    # Convert the fractional part to binary with 100 decimal points
    binary_num += "."

    for _ in range(100):
        fractional_part *= 2
        bit = int(fractional_part)
        binary_num += str(bit)
        fractional_part -= bit

    return binary_num

# Example usage
float_number = 3.14159
binary_representation = float_to_binary(float_number)
print(binary_representation)
