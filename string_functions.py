# String Functions

# There are various built-in methods that can be implemented on strings.

# capitalize():

""" capitalize() changes the first letter of the string into capital letter."""

string_ = "smallletter"  # Declaring a variable with string value.

print(string_.capitalize())

# casefold():

""" casefold() is an aggressive lower() method which converts string to casefolded string."""

caps_string = "APPLE"

print(caps_string.casefold())

# center():

""" center() is used to center a string at the center of certain charcater that are repeating on left and right."""

""" Synatx: variable_name.center(width, fillchar) """

"""
Takes two arguments:

1. width    => It is the complete length of the string that the resulting string must have.
2. fillchar => Which character should be repeated on the left and right.

NOTE : If fillchar is not specified then the default character is space.
"""

print(caps_string.center(24, "g"))

# count()

""" count() is used to count the occurance of a character or a substring in the original string."""

print(string_.count('l'))

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
# backslashreplace    => inserts a \\uNNNN espace sequence instead of unencodable unicode
# namereplace         => inserts a \N{...} escape sequence instead of unencodable unicode

# endswith():

""" Returns True if a string ends with specified suffix."""

print(string_.endswith("letter"))  # Returns True
print(string_.endswith('e'))  # Returns False


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

print(string_.find('let'))


# format_map():     

""" It is similar to format function but takes a single dictionary as input."""

dictionary = {'x': 4, 'y': 5}  # Declaring a dictionary with two key value pair.
print("{x}-{y}".format_map(dictionary))

# index():

""" Returns the initial or start index of a substring inside the string."""
""" Returns value error if substring or character is not found."""

print(string_.index('l'))
print(string_.index('z'))  # Will give value error. 


# join():

""" Used to concatinate any iterable into a single string value.
Only string can be passed in as argument or a list, tuple containing only strings."""

string_list = ['h', 'e', 'l', 'l', 'o']  # Declaring a list of characters.
print("".join(string_list))

# ljust() and rjust():