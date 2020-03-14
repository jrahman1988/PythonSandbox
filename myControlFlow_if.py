'''
Control flow with "if-elif-else" branching
'''

#Searching for and element in a Tuple using 'if-elif-else'
t1: tuple = ("Sylhet", "Chittagong", "Cox's Bazar", "Muroran", "Toronto", "Ottawa", 1960, 1978, 1969, 1990, 1996, 1997)
print(t1)

#Search for an element in the tuple t1, if not present, print it was not found
if "Sunamgonj" in t1:
    print("Sunamgonj is present in the tuple t1")
else:
    print("Sunamgonj is not found in the tuple")

#Search for multiple elements in the tuple t1, if found, print its existance
if ("Geneva" in t1) & ("Paris" in t1):
    print("Both Geneva and Paris are found in the tuple t1")
else:
    print("nothing found")

#Compare and find the largest number
x: int = 500
y: int = 2000
z: int = 300

if (x > y) & (x > z):
    print("x is the largest number ", x)
elif (y > x) & (y > z):
    print("y is the largest number ", y)
else:
    print("z is the largest number ", z)

#Find and replace an element using if..elif..else in a list
l1: list = [10,20,30,40,50]
print("The list are: ", l1)

if l1[2] == 30:
    l1[2] = 300
print("The modified list are now: ", l1)

#Find and replace an element using if..elif..else in a dictionary
d1: dict = {"Apple":'5', "Prune": 4, "Pear": 2, "Blueberry": 7}
print("The dictionary elements are: ", d1)

if d1["Prune"] < 10:
    d1["Prune"] = d1["Prune"] + 7
print("The modified dictionary is now: ", d1)