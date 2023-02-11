# f-string

""" f-string is a formatting method introduced in python 3.6."""
"""
f-strings are a way of formatting strings in Python, introduced in version 3.6. 
They are considered to be more efficient than the traditional .format() method and format specifiers. 
The syntax for f-strings is f"Hello {placeholder}", where values are placed within curly braces {} as placeholders.
"""

age = 20  # Declaring a integer value.

f_string = (
    f"Hello I am {age} old"  # Declaring a formatted string with the help of f-string.
)

print(f_string)

"""
This code declares an integer variable age with the value 20, and then creates an f-string by using the f string syntax
 and placing the age variable inside curly braces {} as a placeholder. Finally, the f-string is printed to the console.
"""
