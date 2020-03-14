'''
Tuple in Python is like an array but only difference is it can contain different types of data in single tuple
Tuple is immutable and defined by specifying items separated by commas with optional parenthesis

Tuples are used to hold together multiple objects. Think of them as similar to lists, but without the extensive functionality that the
list class gives you. One major feature of tuples is that they are immutable like strings i.e. you cannot modify tuples.
Tuples are defined by specifying items separated by commas within an optional pair of parentheses.
Tuples are usually used in cases where a statement or a user-defined function can safely assume that the collection of values (i.e.
the tuple of values used) will not change.
'''

x: tuple = (5.0, True, 4, "Dinajpur", 45.0)

#print the tuple x
print("The tuple has these elements:",x)

#print the first element of the tuple x
print("The first element of the tuple x =",x[0])

#print the last element of the tuple x
print("Last element of the tuple x =",x[-1])

#Find and print the length of a tuple
print('Length of the tuple x =', len(x))