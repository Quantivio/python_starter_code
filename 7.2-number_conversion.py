"""Conversion of decimal values to binary, octal, hexadecimal and vice versa."""

""" Representation of binary, octal, hexadeciml values in python"""

""" Binary      = Begins with '0b'
    Ocatal      = Begins with '0o'
    Hexadeciaml = Begins with '0x'
"""

decimal = 20  # Declaring a decimal value.

# Converting the decimal value to binary value:

""" bin() is the function that converts decimal values to binary."""

print("Conversion of decimal value to binary value: ",bin(decimal))


# Converting the decimal value to octal:

""" oct() is the function that converts decimal values to octal."""

print("Conversion of decimal value to octal value: ",oct(decimal))


# Converting the decimal value to hexadecimal:

""" hex() is the function that converts decimal values to hexadecimal."""

print("Conversion of decimal value to hexadecimal value: ",hex(decimal))


binary = 0b1111  # Declaring a binary value.

# Converting the binary value to decimal:

""" int() is the function that converts binary values to decimal."""

print("Conversion of binary value to decimal value: ",int(binary))


# Converting the binary value to hexadecimal:

print("Conversion of binary value to hexadecimal value: ",hex(binary))


# Converting the binary value to octal:

print("Conversion of binary value to octal value: ",oct(binary))


hexadecimal = 0x10000  # Declaring a hexadecimal value.

# Converting the hexadecimal value to decimal:

print("Conversion of hexadecimal value to decimal value: ",int(hexadecimal))


# Converting the hexadecimal value to binary:

print("Conversion of hexadecimal value to binary value: ",bin(hexadecimal))


# Converting the hexadecimal value to octal:

print("Conversion of hexadecimal value to octal value: ",oct(hexadecimal))


octal = 0o10000  # Declaring a octal value.

# Converting the octal value to decimal:

print("Conversion of octal value to decimal value: ",int(octal))


# Converting the hexadecimal value to binary:

print("Conversion of octal value to binary value: ",bin(octal))


# Converting the hexadecimal value to octal:

print("Conversion of octal value to hexadecimal value: ",hex(octal))

