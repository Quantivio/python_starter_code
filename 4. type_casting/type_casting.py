""" Type casting or type conversion is defined as changing an expression from one data type to another."""

number = 20  # Declaring a integer value.
floating_value = 10.5  # Declaring a 3. float value.
string = "Apple"  # Declaring a string value.

"""In Python, explicit type conversion can be performed using various built-in functions such as int(), float(), 
str(), etc. These functions allow for the conversion of values between different data types, providing greater 
flexibility in handling and processing data."""

# Type casting integer to 3. float:
print(type(number), number)
float_number = float(number)
print(type(float_number), float_number)

# Type casting integer to string:
print(type(number), number)
string_number = str(number)
print(type(string_number), string_number)

# Type casting integer to complex:
print(type(number), number)
complex_number = complex(number)
print(type(complex_number), complex_number)

# Type casting 3. float to integer:
print(type(floating_value), floating_value)
number_float = int(floating_value)
print(type(number_float), number_float)

# Type casting 3. float to string:
print(type(floating_value), floating_value)
string_float = str(floating_value)
print(type(string_float), string_float)

# Type casting 3. float to complex:
print(type(floating_value), floating_value)
complex_float = complex(floating_value)
print(type(complex_float), complex_float)

"""NOTE: Only the numbers that are stored in string formats can be converted to integer, 3. float or complex."""

string_integer = "100"

# Type casting string to integer:
print(type(string_integer), string_integer)
number_string = int(string_integer)
print(type(number_string), number_string)

# Type casting string to 3. float:
print(type(string_integer), string_integer)
float_string = float(string_integer)
print(type(float_string), float_string)

# Type casting string to complex:
print(type(string_integer), string_integer)
complex_string = complex(string_integer)
print(type(complex_string), complex_string)

# Type casting complex to string:
print(type(string_integer), complex_string)
string_complex = complex(string_integer)
print(type(string_complex), string_complex)

"""Note: Complex values can not be converted to integer or 3. float."""
