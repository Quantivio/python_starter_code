number = 20  # Declaring a number.

# Implementation of function as_integer_ratio():

""" Returns a pair of integer values whose ratio is equal to 
the corresponding integer or 3. float value with positive denominator."""

print(number.as_integer_ratio())

# Implementation of function bit_length():

""" This function returns a pair of integers whose ratio is equivalent to the input value, 
expressed as either an integer or a 3. float with a positive denominator."""

print(number.bit_length())

# Implementation of function to_bytes():


"""
The to_bytes method in Python allows for the conversion of an integer into an array of bytes. The method takes in three arguments:

    - length: the number of bytes the integer will be represented as.
    - byteorder: the byte ordering to be used. This can be either 'big' or 'little', where 'big' represents 
        the most significant byte at the start of the byte array and 'little' represents the most significant byte at the end of the byte array.
    - signed: a boolean value indicating whether the integer should be treated as a signed or unsigned value.
    
The resulting array of bytes can be used for a variety of purposes, such as in serialization, file I/O, or data transmission over a network.
"""

print(number.to_bytes(2, byteorder="big", signed=False))
print(number.to_bytes(2, byteorder="little", signed=False))

""" When working with negative numbers, the signed attribute in the to_bytes() method should be set to True. 
This will ensure that the resulting byte representation accurately reflects the sign of the integer."""

negative_number = -20  # Declaring a negative number.

print(negative_number.to_bytes(2, byteorder="big", signed=True))
print(negative_number.to_bytes(2, byteorder="little", signed=True))

# Implementation of function from_bytes():

""" 
The from_bytes method in Python allows for the conversion of an array of bytes into an integer. The method takes in three arguments:

    bytes: the array of bytes to be converted into an integer.
    byteorder: the byte ordering to be used. This can be either 'big' or 'little', where 'big' represents the most significant byte at the start of the byte array and 'little' represents the most significant byte at the end of the byte array.
    signed: a boolean value indicating whether the integer should be treated as a signed or unsigned value.
    
The resulting integer can be used for a variety of purposes, such as in data processing, arithmetic operations, or indexing.
"""

print(int.from_bytes(b"\x00\x14", byteorder="big", signed=False))
print(int.from_bytes(b"\x14\x00", byteorder="little", signed=False))

""" When working with negative numbers, the signed attribute in the from_bytes() method should be set to True. 
This will ensure that the resulting byte representation accurately reflects the sign of the integer."""

print(int.from_bytes(b"\xff\xec", byteorder="big", signed=True))
print(int.from_bytes(b"\xec\xff", byteorder="little", signed=True))
