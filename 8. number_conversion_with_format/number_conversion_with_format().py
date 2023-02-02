# In this code, the format() method is used for number conversion instead of bin(), oct(), hex().

number = 20  # Declaring a decimal value.

# Converting the decimal value to binary:
print("Decimal to binary conversion: {:b}".format(number))

# Converting the decimal value to hexadecimal:
print("Decimal to hexadecimal conversion {:x}".format(number))

# Converting the decimal value to octal:
print("Decimal to octal conversion {:o}".format(number))


binary = 0b1111  # Declaring a binary value.

# Converting the binary value to hexadecimal:
print("Binary to hexadecimal conversion: {:x}".format(binary))

# Converting the binary value to octal:
print("Binary to octal conversion: {:o}".format(binary))


octal = 0o14

# Converting the octal value to binary:
print("Octal to binary conversion: {:b}".format(octal))

# Converting the octal value to hexadecimal:
print("Octal to hexadecimal conversion: {:x}".format(octal))


hexadecimal = 0x10000

# Converting the hexadecimal value to binary:
print("Hexadecimal to binary conversion: {:b}".format(hexadecimal))

# Converting the hexadecimal value to octal:
print("Hexadecimal to octal conversion: {:o}".format(hexadecimal))

# Note: The format() method automatically converts binary, octal, and hexadecimal values to
# integer values automatically when they are passed inside the format().

print("Binary to integer conversion: {}".format(binary))
print("Octal to integer conversion: {}".format(octal))
print("Hexadecimal to integer conversion: {}".format(hexadecimal))
