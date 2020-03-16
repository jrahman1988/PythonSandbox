'''
Using Matplotlib module of Python, draw bar graphs
Note that for plotting the graph the axis values should be in list format
'''
from matplotlib import pyplot as plt
import numpy as np

#Declaration of a dictionary which contains the run recods of a cricket club
runrecords = {'Hossam':143, 'Roshan':76, 'Sushil':133, 'Bala':86, 'Ravi':122, 'Jamil':88}
names = list(runrecords.keys())
runs = list(runrecords.values())
print(names)
print(runs)

#Plot a bar graph from the data (names, runs)
plt.title("Run Graph")
plt.xlabel("Names of the players")
plt.ylabel("Runs scored")
plt.bar(names,runs, color="Green")
plt.grid(True)
plt.show()