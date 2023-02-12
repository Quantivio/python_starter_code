# list

""" 
List is a mutable data structure in python.
List can contain all types of data types.
List can contain duplicate elements.
list is an inbuilt class in python
"""
from typing import Any

# Declaring a list:

list_variable: list[Any] = []  # Declaring an empty list

list_variable_1: list[Any] = list()  # Declaring a list with the help of inbuilt function.

list_one = [1, 2, 3.0, "a", "Hello", 2 + 3j]  # List containing all data types.

"""
Slicing of list is same as Slicing of strings
Please refer string_and_slicing.py for knowing about Slicing.

"""

"""
Reversing a list or a string
"""
string = "Hello"

print(string[::-1])  # Giving the count value -1 will reverse the string.

a = [1, 2, 3]

print(a[::-1])
