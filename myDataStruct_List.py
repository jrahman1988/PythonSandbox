'''
List in Python is like an array but only difference is it can contain different types of data in single list
#List is defined by specifying items separated by commas with square brace
#Items can be deleted or added in a list

A list is a data structure that holds an ordered collection of items i.e. you can store a sequence of items in a list. This is easy to
imagine if you can think of a shopping list where you have a list of items to buy, except that you probably have each item on a
separate line in your shopping list whereas in Python you put commas in between them.
The list of items should be enclosed in square brackets so that Python understands that you are specifying a list. Once you have
created a list, you can add, remove or search for items in the list. Since we can add and remove items, we say that a list is a
mutable data type i.e. this type can be altered.
'''

x: list = ["Banana", 22.1, 45, True, .004]
y: list = ["Roshan", "Hossam", "Bala", "Jamil", "Marcel", "Dan", "Gary", "Anuj"]

#Length of the created list
print("The length of the list x =",len(x))
print("The length of the list y =",len(y))

#Print full list
print("The elements in the list x: ", (x))
print("The elements in the list y: ", (y))

#print last item in the list
print("The last element in the list x =",x[-1])
print("The last element in the list y =",y[-1])

#Add a new item in the list
x.append("Orange")
print("A new item has been added in list x: ", x[-1])

#Remove the first item from the list
print('Before delete the first item ', x)
print('We have', len(x), 'items in the list before delete')
del x[0]
print('After delete the first item ', x)
print('We have', len(x), 'items in the list after delete')

#Remove the last item from the list by pop() method
print('Before delete the first item ', y)
print('We have', len(y), 'items in the list before delete')
y.pop()
print('After delete the first item ', y)
print('We have', len(y), 'items in the list after delete')

#Sort the list
y.sort()
print("The sorted list y: ",y)

#Print the full list y using "for..in" loop
for item in y:
 print(item, end='')
print('\n')