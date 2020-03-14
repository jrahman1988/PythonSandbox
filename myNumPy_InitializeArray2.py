'''
Initialize a numpy array[] with zeros(), full(), arange() and other methods of numpy class
'''
import numpy as np

# Declaring an array with 1 row X 3 colums and filled with all 0s using zeros() method of numpy class
a1 = np.zeros((1, 3))
print(a1, "\n")

# Declaring an array with 4 row X 4 colums and filled with all 0s using zeros() method of numpy class
a2 = np.zeros((4, 4))
print(a2, "\n")

# Declaring an array with 5 row X 5 colums and filled with all 5s using full() method of numpy class
a3 = np.full((5, 5), 5)
print(a3, "\n")

# Declaring one dimensional array with values ranging from 0 to 5 using arange() method of numpy class
a4 = np.arange(0, 5)
print(a4, "\n")

# Declaring one dimensional array with values ranging from 0 to 100 and skipping by 10 using arange() method of numpy class
a5 = np.arange(0, 100, 10)
print(a5, "\n")

# Declaring one dimensional array with values ranging from 0 to 100 and skipping by 10 using random.randint() method of numpy class
a6 = np.random.randint(0, 100, 10)
print(a6, "\n")
