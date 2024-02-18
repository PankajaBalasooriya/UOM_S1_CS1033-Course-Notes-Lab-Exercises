message = input("Enter message: ")
base = int(input("Enter base: "))

encrypted_msg = ""
for char in message:
    quotient = int(ord(char))
    encrypted_char = ""
    while quotient != 0:
        remainder = quotient % base
        quotient = quotient // base
        encrypted_char += str(remainder)
    encrypted_char = encrypted_char[::-1]
    encrypted_msg += encrypted_char
print(encrypted_msg)


