# Complement operator (~):

"""The complement operator flips the bits from 0 => 1 or 1 => 0."""

print(~12)  # Printing the complement of 12

# ~12 = -13

""" Internal working of the complement operator"""

""" Manual calculation"""

""" 2's Complement is the method used to convert negative 
numbers to positive numbers and store them in the computer."""

#   Binary of 12           = 00001100
#   Complement of 00001100 = 11110011

#   Binary of 13                = 00001101
#   Complement of 00001101      = 11110010
#   2's Complement of 11110010  = 11110011  2's complement = 1's complement + 1

# Left shift operator:

""" Shifts the zeroes to the left hand side of the binary value 
i.e shifts the values before the dot."""

print(12 << 2)

""" Internal working of the left shift operator."""

#  Binary of 12                          = 1100.0000
#  Applying left shift of 2 to 1100.0000 = 1100000.00

#  print(int(0b110000)) => 48

# Right shift operator:

""" Shifts the zeroes to the right hand side of the binary value 
i.e shift the values after the dot."""

print(12 >> 2)

""" Internal working of the left shift operator."""

#  Binary of 12                           = 1100.0000
#  Applying right shift of 2 to 1100.0000 = 11.0000000

#  print(int(0b11)) => 3


