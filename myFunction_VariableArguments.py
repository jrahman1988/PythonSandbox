'''
Functions are reusable pieces of programs. They allow us to give a name to a block of statements, allowing us to run that block
using the specified name anywhere in your program and any number of times. This is known as calling the function.

When we declare a starred parameter such as *param, then all the positional arguments from that point till the end are collected
as a tuple called 'param'.

Similarly, when we declare a double-starred parameter such as **param, then all the keyword arguments from that point till the
end are collected as a dictionary called 'param'.
'''
#Define a function which has 3 parameters, fixed length integer value, one variable length tuple (numbers) and one variable length dictionary (phonebook)
def total(a=5, *numbers, **phonebook):
    print('a', a)

    #iterate through all the items in tuple
    for tuple_item in numbers:
        print('tuple_item', tuple_item)

    #iterate through all the items in dictionary
    for key_part_of_Dictionary, value_part_of_Dictionary in phonebook.items():
        print("Key =", key_part_of_Dictionary, "Value =", value_part_of_Dictionary)

#Call function total()
total(10,1,2,3,Jack=1123,John=2231,Inge=1560)

