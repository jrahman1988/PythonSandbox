'''
Using Matplotlib module of Python, draw a scatter plot
'''

# importing package
import matplotlib.pyplot as plt

year = [2014, 2015, 2016, 2017, 2018, 2019]
tutorial_public = [39, 117, 98, 54, 28, 15]
tutorial_premium = [0, 0, 13, 56, 39, 14]

plt.barh(year, tutorial_premium, color="#f3e151")
# careful: notice "bottom" parameter became "left"
plt.barh(year, tutorial_public, left=tutorial_premium, color="#6c3376")

# we also need to switch the labels
plt.xlabel('Number of futurestud.io Tutorials')
plt.ylabel('Year')

plt.show()