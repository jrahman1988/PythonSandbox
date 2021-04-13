'''
A dictionary is like an address-book where we can find the address or contact details of a person by knowing only his/her name
i.e. we associate keys (name) with values
Dictionary is represented by dict class. Pair of keys and values are specified in dictionary using the notation
d = {key1 : value1, key2 : value2 }
When we need to create a dictionary from a list of dictionary by filtering specific keys
'''
# List of dictionary, from here will create another dictionary by filtering multiple keys 'a' and 'c':
d2 = [{"c": 3, "a": 1, "b": 2, "d": 4},
      {"a": 100,  "c": 300, "b": 200, "d": 400},
      {"b": 'Ball', "c": 'Cat', "d": 'Doll', "a": 'Apple'}]

filter_list = ["a", "c"]
d22 = [{k: d[k] for k in filter_list}
       for d in d2 if d in d2]

print("Type of d22: ", type(d22))
print(d22)