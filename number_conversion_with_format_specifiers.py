""" In python format specifiers like %i can be used"""
""" Using the format specifiers number conversions can be made."""

"""Format specifiers:
%i => Integer or Decimal 
%s => String
%c => Character
%f => Float
%x => Hexadecimal
%o => Octal
"""

# There is no format specifier for binary.

number = 20  # Decimal a number.

# Conversion of decimal to octal, hexadecimal with format specifiers:

print("Ocatl: %o\nHexadecimal: %x" % (number, number))


# Conversion of binary to decimal, octal, hexadecimal with format specifiers:

binary = 0b1001

print("Decimal: %i\nOcatl: %o\nHexadecimal: %x" % (binary, binary, binary))


# Conversion of octal to decimal, octal, hexadecimal with format specifiers:

octal = 0o1001

print("Decimal: %i\nHexadecimal: %x" % (octal, octal))


# Conversion of hexadecimal to decimal, octal,  with format specifiers:

hexadecimal = 0x100

print("Decimal: %i\nOctal: %x" % (hexadecimal, hexadecimal))


""" %b can't be used for converting to binary."""
