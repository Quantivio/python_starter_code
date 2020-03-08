""" In python a single character or sequence of characters is treated as a string."""

"""There are two techniques indexing and slicing that can be applied to strings in Python."""

""" Indexing is technique used to view a single character from a string."""

""" In python indexing starts form 0."""

variable_name = "Hello"  # Declaring a string.

"""
H e l l o
0 1 2 3 4
"""

""" Indexing Syntax: variable_name[index_value] """

# Indexing to view character e from variable_name:

print(variable_name[1])

# Indexing to view character l from variable_name:

print(variable_name[2])

""" String slicing is a very powerful technique that can be used very easily in python."""

""" Slicing is the technique used to cut of a substring from a string and view it."""

""" 
There are two types of slicing in python:
1. Positional slicing
2. Negative slicing

"""

""" Slicing Syntax: variable_name[start_index:stop_index:step_count] """

""" 
start_index => From were the slicing has to start
stop_index => Where the slicing has to stop and stop_index is always (n - 1) Ex: 9 => (9 - 1 = 8)
step_count => How many characters should be skipped when slicing. 

"""

""" POSITIVE SLICING """

slice_variable = "Antidisestablishmentarianism"

""" 
A n t i d i s e s t  a  b  l  i  s  h  m  e  n  t  a  r  i  a  n  i  s  m
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
"""

# Slicing 'establishment' from slice_variable:

print(slice_variable[7:20])

# Here stop index is 20 so it is 19 = 20 - 1 hence it stops at 't'.

# How to get all the characters before certain index value:

print(slice_variable[:23]) 

# To get all the values before certain index value just specify the stop_index alone.

# How to get all the characters after certain index value:

print(slice_variable[7:]) 

# To get all the values after certain index value just specify the start_index alone.

""" Using the step_count to skip characters """

""" 
The step_count works in such a way that it splits the given value into 1 + remaining.
    For example:
    If step_count is 2 => It is split into 1 + 1
    If step_count is 3 => It is split into 1 + 2
    If step_count is 4 => It is split into 1 + 3
"""

#Using step_count to skip 2 values:

print(slice_variable[7:20:3]) 

""" 
In this example it works as 1 + 3 so that 1 character is accepted and 2 characters are skipped.
    'e' - 1 is accepted and 'st' - 2 are skipped.
    'a' - 1 is accepted and 'bl' - 2 are skipped.
    'i' - 1 is accepted and 'sh' - 2 are skipped.
    'm' - 1 is accepted and 'en' - 2 are skipped.
    't' - 1 is accepted and there are no more characters.
"""

