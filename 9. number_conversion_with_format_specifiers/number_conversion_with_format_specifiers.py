""" In python, number conversions can be made using format specifiers."""

"""Available format specifiers:
%d => Decimal (base 10)
%x => Hexadecimal (base 16)
%o => Octal (base 8)
%s => String
%c => Character
%f => Float
"""

number = 20  # A decimal number.

# Conversion of decimal to octal and hexadecimal using format specifiers:
print("Octal representation: %o" % number)
print("Hexadecimal representation: %x" % number)

binary = 0b1001  # A binary number.

# Conversion of binary to decimal, octal, and hexadecimal using format specifiers:
print("Decimal representation: %d" % binary)
print("Octal representation: %o" % binary)
print("Hexadecimal representation: %x" % binary)

octal = 0o1001  # An octal number.

# Conversion of octal to decimal and hexadecimal using format specifiers:
print("Decimal representation: %d" % octal)
print("Hexadecimal representation: %x" % octal)

hexadecimal = 0x100  # A hexadecimal number.

# Conversion of hexadecimal to decimal and octal using format specifiers:
print("Decimal representation: %d" % hexadecimal)
print("Octal representation: %o" % hexadecimal)
