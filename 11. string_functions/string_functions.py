# String Functions

# There are various built-in methods that can be implemented on strings.

# capitalize():

""" capitalize() changes the first letter of the string into capital letter."""
from typing import Any

string_ = "small-letter"  # Declaring a 1. variable with string value.

print(string_.capitalize())

# casefold():

""" casefold() is an aggressive lower() method which converts string to case-folded string."""

caps_string = "APPLE"

print(caps_string.casefold())

# center():

""" center() is used to center a string at the center of certain character that are repeating on left and right."""

""" Syntax: variable_name.center(width, fillchar) """

"""
Takes two arguments:

1. width    => It is the complete length of the string that the resulting string must have.
2. fillchar => Which character should be repeated on the left and right.

NOTE : If fillchar is not specified then the default character is space.
"""

print(caps_string.center(24, "g"))

# count()

""" count() is used to count the occurrence of a character or a substring in the original string."""

print(string_.count("l"))

# encode()

""" encode() returns an encoded version of the string."""

""" Syntax: variable_name.encode(encoding, errors) """

""" 
Takes two arguments:

1. encoding => Any supported encoding format in python.
2. errors   => Response when encoding fails.

"""

# Errors:
# strict              => default response which raises a UnicodeDecodeError exception on failure.
# ignore              => ignores the unencodable unicode from the result
# replace             => replaces the unencodable unicode to a question mark ?
# xmlcharrefreplace   => inserts XML character reference instead of unencodable unicode
# backslashreplace    => inserts a \\uNNNN space sequence instead of unencodable unicode
# name-replace         => inserts a \N{...} escape sequence instead of unencodable unicode

# endswith():

""" Returns True if a string ends with specified suffix."""

print(string_.endswith("letter"))  # Returns True
print(string_.endswith("e"))  # Returns False

# expandstab():

""" Syntax: variable_name.expandstab(tabsize=8)
"""

""" 
* Expands a tab space into white spaces passed as argument.
* Default tabsize is 8.
"""

print("    Hello".expandtabs(20))

# find():

""" Used to find a substring or a character in a string."""

""" It returns the starting index of the substring or return -1 if the substring is not found."""

print(string_.find("let"))

# format_map():

""" It is similar to format function but takes a single dictionary as input."""

# Declaring a dictionary with two key value pair.
dictionary_ = {"x": 4, "y": 5}
print("{x}-{y}".format_map(dictionary_))

# index():

""" Returns the initial or start index of a substring inside the string."""
""" Returns value error if substring or character is not found."""

print(string_.index("l"))
# print(string_.index('z'))  # Will give value error.


# join():

""" Used to concatenate any iterable into a single string value.
Only string can be passed in as argument or a list, tuple containing only strings."""

string_list = ["h", "e", "l", "l", "o"]  # Declaring a list of characters.
print("".join(string_list))

# ljust() and rjust():

""" This methods will return a left-justified or right-justified string based on the given width."""

""" Syntax: variable_name.ljust(width, fillchar)"""

""" 
width => It is the complete length of the string that the resulting string must have.
fillchar => Minimum width of the string.
NOTE : If fillchar is not specified then the default character is space. """

animal = "cat"  # Declaring a string.

print(animal.ljust(10, "*"))  # Left justify.

print(animal.rjust(10, "*"))  # Right justify.

# lower() and upper():

""" Used to convert a lower-case string to upper-case and vice versa. """

lower_case = "abcd"  # Declaring a string.

upper_case = "ABCD"  # Declaring a string.

print(lower_case.upper())

print(upper_case.lower())

# strip(), lstrip() and rstrip():

""" Used to remove any repeating characters from a string from both sides. """

""" This method takes one argument i.e the repeating character that must be removed. """

""" When no argument is passed the default argument is space. """

repeated_string = "qqqqqqqPythonqqqqq"  # Declaring a string.
# Declaring a string.
repeated_string_space = "         qqqqqqqPythonqqqqq               "

print(repeated_string.strip("q"))

# When no argument is passed the default argument is space.
print(repeated_string_space.strip())

left_repeat = "qqqqqApple"  # Declaring a string.

right_repeat = "Appleqqqqq"  # Declaring a string.

print(left_repeat.lstrip("q"))

print(right_repeat.rstrip("q"))

# maketrans():

""" Maketrans returns a mapping table that can be used for translation using the translate() method."""
""" Maketrans can be useful for translating various characters with other characters in a particular string."""

""" Syntax: string.maketrans(x=dict, y, z)
* y and z are optional.
"""

string = "abc"  # Declaring string value.

dictionary: dict[str, Any] = {"a": "123", "b": "456", "c": "789"}

print(table := string.maketrans(dictionary))  # Using walrus operator.

# translate():

"""Used to replace number individual characters to 
another character with the help of translation table obtained from maketrans() method."""

"""Syntax : string.translate(table)"""

print(string.translate(table))

# replace():

""" It is used to replace a character or a substring in a string."""

"""Syntax: string.replace(old, new, count)

old => It is the string that is to be replaced.
new => It is the string that is going to replace the old string.

"""

word = "hello"

print(word.replace("l", "y"))

# partition():

""" It is uses to separate a string based on the seperator passes as argument. It returns a tuple as output."""

""" Syntax: 1. variable.partition(seperator)"""

sentence = "Hello I am good"

print(sentence.partition("am"))

# splitlines():

""" Used to split a string based on escape sequence like \n and \r."""

# String value with escape sequence.
value = "Hello \n world \r I am born in India."

print(value.splitlines())

"This function has parameter called keepend=False if set to True it will also show the escape sequence."

print(value.splitlines(True))

# zfill():

"""This function will return a copy of the string with '0' padded on the left side of the string based on the 
specified width."""

"""If a string width is 5 but the parameter inside zfill() iss 10 then 5 '0' will be padded on the left side of the 
string."""

st = "hello"

print(st.zfill(10))

# rfind():

"""This function is similar to find() but starts checking for the character or substring from the right side of the 
string."""

print("appleapple".rfind("l"))

# rindex():

"""This function is similar to index() but starts checking for the character or substring from the right side of the 
string."""

print("appleapple".rindex("l"))

# swapcase():

""" This function converts all the upper case letters to lower case and vice versa."""

print("AbCdEf".swapcase())
