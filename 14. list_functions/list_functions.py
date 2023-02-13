# List Functions

# 1. append()
# append() function adds an element to the end of a list.

a = [1, 2, 3]  # Declaring a list.

a.append(4)

print("After appending:", a)  # After appending print the list.

# 2. clear()
# clear() function clears all the elements in a list and makes it empty.

a = ["a", 1, 2, 4.0]

print("Before clearing:", a)  # Printing the list before clearing.

a.clear()

print("After clearing:", a)  # Returns an empty list since the list is cleared.

# 3. count() and index()
# count() and index() functions work in the same way as their string counterparts.
# For more information, refer to the file string_functions.py

# 4. copy()
# copy() makes a shallow copy of a list.
# Shallow copy means that any changes made to the copied list will not affect the original list.

a = [1, 2, 3]

b = a.copy()  # Making a shallow copy of the list 'a'.

# Printing a and b before changing values.

print("Before changes:", a)
print("Before changes:", b)

b.remove(1)  # Changing a value in b.

# Printing after making changes.

print("After changes:", a)
print("After changes:", b)

# 5. insert()
# insert() is used to insert an element at the desired position or index in a list.
# Syntax: list.insert(index, object)

a = [1, 2, 3]

a.insert(0, 5)  # Inserting 5 at the index position 0.

print("After inserting:", a)

# 6. extend()
# extend() adds a set of iterables to the end of a list.

a = [1, 2, 3]

a.extend([4, 5, 6, 100, 200])

print("After extending:", a)

# 7. pop()
# pop() removes an element from a list based on its index position.
# If no arguments are passed, pop() removes the last element in a list and returns the removed value.

a = [1, 2, 3]

print("Removed element:", a.pop())  # Since no argument is passed, pop removes the last element.

print("After popping:", a)

a = [1, 2, 3, 4]

print("Removed element:", a.pop(1))  # Passing the index value as 1.

print("After popping:", a)

# 8. remove()
# remove() removes an element from a list without its index position.
# The element to be removed from the list should be passed as an argument.

a = [100, 200, 300]

a.remove(200)

print("After removing:", a)

# 9. reverse()
# reverse() reverses a list.

a = [50, 60, 70, 80, 90, 100]

a.reverse()

print("After reversing:", a)

# 10. sort()

"""
sort() is used to sort a list in ascending order by default.
"""

a = [7, 10, 2, 1, 0, 65, 78]

a.sort()

print("Sorted list in ascending order: ", a)

# To sort a list in descending order, we can use the reverse parameter.
a.sort(reverse=True)

print("Sorted list in descending order: ", a)
