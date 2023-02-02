# Printing to the Console with the print() Function

# A string can be specified with either single quotes '' or double quotes "".
print('Hello world! within single quotes.')
print("Hello world! within double quotes.")

# Variables can be used inside the print() method to display to the console.
age = 20
year = 2000

# Printing a variable using commas:
print("My age is", age)

# Printing a variable using typecasting and the + (concatenation) operator:
print("My age is " + str(age) + " and I was born in " + str(year))

# Printing a variable using the .format() method:
print("My age is {} and I was born in {}".format(age, year))

# The parameters that are passed inside the .format() method have index values:
# .format(value_one, value_two) where value_one has index 0 and value_two has index 1.

# Using the .format() method and indexing:
print("I was born in {1} and my age is {0}".format(age, year))
