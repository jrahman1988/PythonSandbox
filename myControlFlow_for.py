'''
The for..in statement is a looping statement which iterates over a sequence of objects i.e. go through each item in a
sequence. We will see more about sequences in detail in later chapters. What you need to know right now is that a sequence is just
an ordered collection of items.
'''

l1: list = ["White", "Red", "Yellow", "Green", "Black"]
l2: list = ["Car", "Umbrella", "Bag"]

#Print the items in both list using for..in loop
print("First list l1:")
for i in l1:
    print(i)

print("First list l2:")
for i in l2:
    print(i)

#Usage of inner loop and print the items from both list
for i in l1:
    for j in l2:
        print(i, j)
