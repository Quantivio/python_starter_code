number = 20 #Declaring a number.


# Implementation of function as_integer_ratio():

""" Returns a pair of integer values whose ratio is equal to 
the corresponding integer or float value with positive denominator."""

print(number.as_integer_ratio())


# Implementation of function bit_length():

""" Returns a integer value which represents the number of bits 
needed to represent the decimal number in binary form."""

print(number.bit_length())


# Implementation of function to_bytes():

""" Returns an array of bytes representing an integer."""

"""Syntax: variable.to_bytes(length, byteorder='big' or 'little', signed=True or False)"""

""" 'big' = Most significant byte is at the start of the byte array.
    'little' = Most significant byte is at the end of the byte array.
"""

print(number.to_bytes(2, byteorder='big', signed=False))
print(number.to_bytes(2, byteorder='little', signed=False))

""" For negative number only the signed attribute can be set to True."""

negative_number = -20 # Declaring a negative number.

print(negative_number.to_bytes(2, byteorder='big', signed=True))
print(negative_number.to_bytes(2, byteorder='little', signed=True))

