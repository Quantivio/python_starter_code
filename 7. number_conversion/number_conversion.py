"""Conversion of decimal values to binary, octal, hexadecimal and vice versa."""

""" Representation of binary, octal, hexadecimal values in python"""

""" Binary      = Begins with '0b'
    Octal      = Begins with '0o'
    Hexadecimal = Begins with '0x'
"""

decimal = 20

# Conversion of decimal to binary, octal, and hexadecimal
print("Decimal:", decimal)
print("Binary:", bin(decimal))
print("Octal:", oct(decimal))
print("Hexadecimal:", hex(decimal))

binary = 0b1111

# Conversion of binary to decimal, octal, and hexadecimal
print("\nBinary:", binary)
print("Decimal:", int(binary))
print("Octal:", oct(binary))
print("Hexadecimal:", hex(binary))

hexadecimal = 0x10000

# Conversion of hexadecimal to decimal, binary, and octal
print("\nHexadecimal:", hexadecimal)
print("Decimal:", int(hexadecimal))
print("Binary:", bin(hexadecimal))
print("Octal:", oct(hexadecimal))

octal = 0o10000

# Conversion of octal to decimal, binary, and hexadecimal
print("\nOctal:", octal)
print("Decimal:", int(octal))
print("Binary:", bin(octal))
print("Hexadecimal:", hex(octal))
