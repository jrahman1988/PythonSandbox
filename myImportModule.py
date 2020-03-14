'''
Import module and then find what are inside that module
'''
import numpy as np
print(dir(np))

aList:  list = [1,2,3,4,5,6,7,8,9]
print(aList)

a = np.average(aList)
print("Average of all the numbers in the list a =", a)

b = np.add(1.0, 2.0)
print("Sum of all the numbers in the list b =", b)