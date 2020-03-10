""" print() function is to show output to the console or the user."""

"""A string inside print function can be specified with either singlequotes '' or doublequotes "" print()."""

# print() with singlequotes:

print('Hello world! within singlequotes.')

# print() with doublequotes:

print("Hello world! within doublequotes.")


""" Variable that are used can be used inside the print() method to be displayed to the console."""

"""Various methods can be used to print variable using print() method."""

age = 20  # Declaring a integer value.
year = 2000  # Declaring a integer value.


# Printing variable using commas:

print("My age is ", age)

# Printing variable using typecasting and + (concatination) operator:

print("My age is "+str(age)+" and I am born in "+str(year))

# Printing variable using .format() method:

print("My age is {} and I am born in {}".format(age, year))

""" The parameters that are passed inside .format() method have index values."""
""" .format(value_one, value_two) here value_one has index 0 and value_two has index 1."""

# Using .format() and indexing:

# print("I am born in {} and my age is {}".format(age, year)) => "I am born in 20 and my age is 2000"

print("I am born in {1} and my age is {0}".format(age, year))

