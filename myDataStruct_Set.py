'''
Sets are unordered collections of simple objects. These are used when the existence of an object in a collection is more important
than the order or how many times it occurs.
Using sets, you can test for membership, whether it is a subset of another set, find the intersection between two sets, and so on.
'''

s1: set = {"Jamil", 45.5, "Hasan", 100, "Rosahn", True}
s2: set = {"Shelley", "AMD", "Raga", "Test Solutions", "Hemanth", "Ford", "Hasan", 100}
print('Set s1: ',s1)
print('Set s2: ',s2)

#Add a new elements in a set
s1.add("Hello World")
print("After adding a new item (Hello World) in set s1: ", s1)
s1.add(3+4j)
print("After adding another new item (3+4j) in set s1: ", s1)

#Update a set with union of iteself or others
s1.update(s2)
print('After joining set s2 to set s1 : ',s1)
