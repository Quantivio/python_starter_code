# Bitwise Operators in Python:

# Complement Operator (~)

# The complement operator flips the bits of a binary number, converting 0s to 1s and 1s to 0s.

#   Binary of 12           = 00001100
#   Complement of 00001100 = 11110011

#   Binary of 13                = 00001101
#   Complement of 00001101      = 11110010
#   2's Complement of 11110010  = 11110011  2's 5. complement = 1's 5. complement + 1

print(~12)  # Output: -13

# The above line of code uses the 2's complement method to convert a negative number to positive and store it in the computer.
# Here, the binary representation of 12 is 00001100, and the complement of this number is 11110011.
# The 2's complement of 11110011 is 11110011, which is equal to the 1's complement + 1.

# Left Shift Operator (<<)

# The left shift operator shifts the bits of a binary number to the left, effectively multiplying the number by 2^n (where n is the number of shifts).

#  Binary of 12                          = 1100.0000
#  Applying left shift of 2 to 1100.0000 = 1100000.00

#  print(int(0b110000)) => 48

print(12 << 2)  # Output: 48

# The binary representation of 12 is 1100.0000, and after applying the left shift operator by 2, it becomes 1100000.00.
# Converting the binary number back to decimal gives us the output 48.

# Right Shift Operator (>>)

# The right shift operator shifts the bits of a binary number to the right, effectively dividing the number by 2^n (where n is the number of shifts).

# Internal working of the right shift operator

#  Binary of 12                           = 1100.0000
#  Applying right shift of 2 to 1100.0000 = 11.0000000

#  print(int(0b11)) => 3

print(12 >> 2)  # Output: 3

# The binary representation of 12 is 1100.0000, and after applying the right shift operator by 2, it becomes 11.0000000.
# Converting the binary number back to decimal gives us the output 3.
