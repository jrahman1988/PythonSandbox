'''
A dictionary is like an address-book where we can find the address or contact details of a person by knowing only his/her name
i.e. we associate keys (name) with values
Dictionary is represented by dict class. Pair of keys and values are specified in dictionary using the notation
d = {key1 : value1, key2 : value2 }
'''

#Ddeclaration of a dictionary
d1: dict = {"Rafi":"rafi@me.com", "Wahid":'wahid@ieee.com', "Jamil":'jamil@innovapost.com', "Cyrus":'cyrus@lenova.ca', "Mango":45.50, "Orange":70.35, "banana":15.90}
print(d1)

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
