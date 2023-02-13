# String Functions

# There are various built-in methods that can be implemented on strings.


# capitalize():
""" capitalize() changes the first letter of the string into capital letter."""
string_ = "small-letter"  # Declaring a variable with string value.
print("Capitalized string:", string_.capitalize())

# casefold():
""" casefold() is an aggressive lower() method which converts string to case-folded string."""
caps_string = "APPLE"
print("Casefolded string:", caps_string.casefold())

# center():
""" center() is used to center a string at the center of certain character that are repeating on left and right."""
""" Syntax: variable_name.center(width, fillchar) """
"""
Takes two arguments:

1. width    => It is the complete length of the string that the resulting string must have.
2. fillchar => Which character should be repeated on the left and right.

NOTE : If fillchar is not specified then the default character is space.
"""
print("Centered string:", caps_string.center(24, "g"))

# count()
""" count() is used to count the occurrence of a character or a substring in the original string."""
print("Number of occurrences of 'l' in the string:", string_.count("l"))

# encode()
""" encode() returns an encoded version of the string."""
""" Syntax: variable_name.encode(encoding, errors) """
""" 
Takes two arguments:

1. encoding => Any supported encoding format in python.
2. errors   => Response when encoding fails.

"""

string_ = "letter"

# endswith():

""" Returns True if a string ends with specified suffix."""

print(string_.endswith("letter"))  # Returns True
print(string_.endswith("e"))  # Returns False

# expandstab():

""" Syntax: variable_name.expandtabs(tabsize=8)
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

print(string_.ljust(10, "."))
print(string_.rjust(10, "."))

animal = "cat"

# Left justify
print(animal.ljust(10, "*"))

# Right justify
print(animal.rjust(10, "*"))

# lower() and upper():

# Declaring a lower-case string
lower_case = "abcd"

# Declaring an upper-case string
upper_case = "ABCD"

# Converting lower-case to upper-case
print(lower_case.upper())

# Converting upper-case to lower-case
print(upper_case.lower())

# strip(), lstrip() and rstrip():

# Declaring a string with repeating characters
repeated_string = "qqqqqqqPythonqqqqq"

# Declaring a string with repeating spaces
repeated_string_space = "         qqqqqqqPythonqqqqq               "

# Removing repeating characters from the string
print(repeated_string.strip("q"))

# Removing repeating spaces from the string
print(repeated_string_space.strip())

# Declaring a string with repeating characters on the left side
left_repeat = "qqqqqApple"

# Declaring a string with repeating characters on the right side
right_repeat = "Appleqqqqq"

# Removing repeating characters from the left side of the string
print(left_repeat.lstrip("q"))

# Removing repeating characters from the right side of the string
print(right_repeat.rstrip("q"))

# maketrans():

# Declaring a string value
string = "abc"

# Creating a dictionary to store the mapping of characters
dictionary = {"a": "123", "b": "456", "c": "789"}

# Using the walrus operator to assign the value of the mapping table to a variable
print(table := string.maketrans(dictionary))

# translate():

# Replacing characters in the string using the mapping table obtained from maketrans()
print(string.translate(table))

# replace():

# Declaring a word
word = "hello"

# Replacing a character in the word
print(word.replace("l", "y"))

# partition():

# Declaring a sentence
sentence = "Hello I am good"

# Separating the sentence based on the separator "am" and returning a tuple
print(sentence.partition("am"))

# splitlines():

"""Used to split a string into separate lines based on escape sequences, such as \n and \r."""

value = "Hello \n world \r I am born in India."

# splitlines() without the keepend parameter
print("splitlines() without keepend:", value.splitlines())

# splitlines() with keepend set to True
print("splitlines() with keepend=True:", value.splitlines(True))

# zfill():

"""Returns a copy of the string with '0' characters padded on the left side, based on the specified width."""

string = "hello"

# padding the string with 5 '0' characters
print("zfill() with width=10:", string.zfill(10))

# rfind():

"""Searches for the specified substring in the string, starting from the right side of the string."""

print("rfind() result:", "appleapple".rfind("l"))

# rindex():

"""Similar to rfind(), but raises an error if the substring is not found."""

print("rindex() result:", "appleapple".rindex("l"))

# swapcase():

"""Converts upper case characters to lower case, and vice versa."""

print("swapcase() result:", "AbCdEf".swapcase())
