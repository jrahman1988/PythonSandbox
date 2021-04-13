'''
A dictionary is like an address-book where we can find the address or contact details of a person by knowing only his/her name
i.e. we associate keys (name) with values
Dictionary is represented by dict class. Pair of keys and values are specified in dictionary using the notation
d = {key1 : value1, key2 : value2 }
'''

# Single dictionary: filtering specific keys and create another dictionary
d1 = {"c": 3, "a": 1, "b": 2, "d": 4}
d11 = dict((i, d1[i])
           for i in ["a", "c"] if i in d1)
print(type(d11))
print(d11)

# List of dictionary: filtering specific keys and create another dictionary
d2 = [{"c": 3, "a": 1, "b": 2, "d": 4},
      {"a": 100,  "c": 300, "b": 200, "d": 400},
      {"b": 'Ball', "c": 'Cat', "d": 'Doll', "a": 'Apple'}]

filter_list = ["a", "c"]
d22 = [{k: d[k] for k in filter_list} for d in d2]
print(type(d22))
print(d22)

# List of dictionary: extract values of a specific keys in a list
d3 = [{'a': 1.0, 'b': 2.0},
 {'a': 3.0, 'b': 4.0},
 {'a': 5.0, 'b': 6.0},
 {'a': 7.0, 'b': 9.0},
 {'a': 9.0, 'b': 0.0}]

d33 = [i["a"] for i in d3]
print(type(d33))
print(d33)

# Other dictionary exampled
d1: dict = {"Rafi":"rafi@me.com", "Wahid":'wahid@ieee.com', "Jamil":'jamil@innovapost.com', "Cyrus":'cyrus@lenova.ca', "Mango":45.50, "Orange":70.35, "banana":15.90}
print(d1)
#
#Print the dictionary in "(Key:value)" format using item() method
print("Here are the items in the dictioanry d1: ",d1.items())

#Print only the keys
print("Here are the keys in the dictionaty d1: ", d1.keys())

#Print only the values
print("Here are the values in the dictionary: ", d1.values())

#Print size of a dictionary
print("The length of the dictionary d1 =", len(d1))

#Add and print one element in an existing dictionary
d1["Shipar"] = 'jamilur_rahman@yahoo.com'
print(d1)

#Print all keys in the dictionary using for..in
for name in d1.keys():
    print('The keys in the dictionary are: {}'.format(name))

#Print all items in the dictionary using for..in
for value in d1.values():
    print('The items in the dictionary are: {}'.format(value))
