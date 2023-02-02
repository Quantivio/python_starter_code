# In Python, a single character or a sequence of characters is treated as a string.
# Strings can be manipulated in Python using two techniques: indexing and slicing.

# Indexing is used to view a single character from a string.
# Indexing in Python starts from 0.

variable_name = "Hello"

# Declaring a string
# H e l l o
# 0 1 2 3 4

# To access a character in a string using indexing, use the following syntax:
# variable_name[index_value]

# To view the character 'e' from variable_name:
print(variable_name[1])

# To view the character 'l' from variable_name:
print(variable_name[2])

# Slicing is a powerful technique to cut off a substring from a string and view it.
# There are two types of slicing in Python:
# 1. Positional slicing
# 2. Negative slicing

# To perform slicing on a string, use the following syntax:
# variable_name[start_index:stop_index:step_count]
# start_index: The starting point of the slicing
# stop_index: The end point of the slicing, where the slicing stops. The stop_index is always (n-1).
# For example, if the stop_index is 9, it means the slicing will stop at the 8th position.
# step_count: The number of characters to skip during slicing.

# Positional Slicing

slice_variable = "Antidisestablishmentarianism"

# Declaring a string
# A n t i d i s e s t  a  b  l  i  s  h  m  e  n  t  a  r  i  a  n  i  s  m
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27

# To slice the word 'establishment' from slice_variable:
print(slice_variable[7:20])

# To get all the characters before a certain index value:
print(slice_variable[:23])

# To get all the characters after a certain index value:
print(slice_variable[7:])

# To skip characters using step_count:
# The step_count splits the characters into 1 + remaining.
# For example, if step_count is 2, it means 1 character is accepted and 1 character is skipped.
# If step_count is 3, it means 1 character is accepted and 2 characters are skipped.

print(slice_variable[7:20:3])

# Negative Indexing
# Negative indexing is used to access characters from the right end of the string, starting from -1.

# In the string slice_variable, negative indexing can be used as follows:
# A   n   t   i   d   i   s   e   s   t   a   b   l   i   s   h   m   e   n   t   a   r   i   a   n   i   s   m
# -28 -27 -26 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -15 -14 -13 -12  -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# Accessing the Last Element using Negative Indexing

# Negative indexing starts from -1, which represents the last element of the string.
# The following code retrieves the last element of the string 'slice_variable'

print("Last element of slice_variable:", slice_variable[-1])


# Accessing the Element before the Last using Negative Indexing

# Negative indexing starts from -1, and the value of negative index increases as we go towards the first element of the string.
# The following code retrieves the 20th element from the end of the string 'slice_variable'

print("20th element from the end of slice_variable:", slice_variable[-20])


# Negative Slicing

# Negative slicing is used to extract substrings from a string using negative indexes.
# Negative indexes represent the position of elements starting from the end of the string.
# The following code demonstrates negative slicing of the string 'slice_variable'.

# Negative slicing with start_index and stop_index

# To perform negative slicing, we need to specify the start_index and stop_index (inclusive and exclusive respectively).
# The most common error in negative slicing is providing a higher start_index value on the left and a lower stop_index value on the right.
# The following code retrieves an empty string as the result of the slicing.

print("Negative slicing with start and stop index:", slice_variable[-1:-3])


# Negative slicing to extract 'establishment'

# The following code retrieves the substring 'establishment' using negative slicing

print("Extracted substring using negative slicing:", slice_variable[-21:-8])


# Negative slicing with step_count

# The step_count argument is used to skip a specific number of elements while slicing.
# The following code skips 2 elements while performing negative slicing.

print("Negative slicing with step_count:", slice_variable[-21:-8:3])
