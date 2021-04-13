'''
Using Matplotlib module of Python, draw a scatter plot
'''

# importing package
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# # create data
# df = pd.DataFrame([['A', 10, 20, 10, 30], ['B', 20, 25, 15, 25], ['C', 12, 15, 19, 6],
# 				['D', 10, 29, 13, 19]],
# 				columns=['Team', 'Round 1', 'Round 2', 'Round 3', 'Round 4'])
# # view data
# print(df)
#
# # plot grouped bar chart
# df.plot(x='Team',
# 		kind='bar',
# 		stacked=False,
# 		title='Grouped Bar Graph with dataframe')
#
#

# create data
x = np.arange(5)
y1 = [34, 56, 12, 89, 67]
y2 = [12, 56, 78, 45, 90]
y3 = [14, 23, 45, 25, 89]
width = 0.2

# plot data in grouped manner of bar type
plt.bar(x-0.2, y1, width, color='cyan')
plt.bar(x, y2, width, color='orange')
plt.bar(x+0.2, y3, width, color='green')
plt.xticks(x, ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'])
plt.xlabel("Teams")
plt.ylabel("Scores")
plt.legend(["Round 1", "Round 2", "Round 3"])
plt.show()
