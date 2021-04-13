'''
A dictionary is like an address-book where we can find the address or contact details of a person by knowing only his/her name
i.e. we associate keys (name) with values
Dictionary is represented by dict class. Pair of keys and values are specified in dictionary using the notation
d = {key1 : value1, key2 : value2 }
When we need to create a dictionary from a dictionary by filtering specific keys
'''
# Single dictionary, from here will create another dictionary by filtering out keys 'a' and 'c':
d1 = {"c": 3, "a": 1, "b": 2, "d": 4}

filter_list = ["a", "c"]
d11 = dict((i, d1[i])
           for i in filter_list if i in d1)
print("Type of d11: ", type(d11))
print(d11)