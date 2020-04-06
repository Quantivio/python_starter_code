# List Functions

"""

1. append():
append() function will add element to the end of a list.

"""

a = [1, 2, 3] # Declaring a list.

a.append(4)

print(a) # After appending print the list.

""" 
2. clear():
clear() function clears all the elements in a list and will make it empty.
"""

a = ["a", 1, 2, 4.0]

print(a) # Printing the list before clearing.

a.clear()

print(a) # Returns an empty list since the list is cleared.

""" 
3. count() and index():
count() and index() works as same as the string functions
Refer: string_functions.py
"""

"""
4. copy():
copy() makes a shallow coppy of the list.
Shallow copy means any changes made to the copied list will not affect the original list.
"""
a = [1, 2, 3]

b = a.copy() # Making a shallow copy of a.

# Printing a and b before changing values.

print(a) 
print(b)

b.remove(1) # Changing a value in b.and

# Printing after making changes.

print(a)
print(b)

"""
5. insert()
insert() is used to inser a element in the desired position or index in a list.
Sytax:
list.insert(index, object)
"""

a = [1, 2, 3]

a.insert(0, 5) # Inserting 5 at the index position 0.

print(a)

"""
6. extend()
extend() is used to add a set of iterables to the end of a list.
"""

a = [1, 2, 3]

a.extend([4,5,6,100,200])

print(a)

"""
7. pop()
pop() is used to remove an element from the list based on the index position.
when no arguments are passed pop() removes the last element in a list.
"""

a = [1, 2, 3]

print(a.pop()) # Since no argument is passed pop removes the last element. pop() returns the removed value.

print(a)

a = [1, 2, 3, 4]

print(a.pop(1)) # Passing the index value as 1.

print(a)

"""
8. remove()
remove() is used to remove an element from the list without index position. The element which needs to be removed from the list should be passed as argument.
"""

a = [100, 200, 300]

a.remove(200)

print(a)

"""
9. reverse()
reverse() is used to reverse a list.
"""

a = [50, 60, 70, 80, 90 ,100]

a.reverse()

print(a)

"""

10. sort()
sort is used to sort a list in ascending order.

"""

a = [7, 10, 2, 1,0, 65, 78]

a.sort()

print(a)