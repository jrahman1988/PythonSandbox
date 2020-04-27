import pandas as pd
import requests
import datetime
from matplotlib import pyplot as plt
from sklearn import linear_model
import numpy as np

#Format the date time to present on the graph
currentDateTime = datetime.datetime.now()
print("Current Date Time: {}".format (currentDateTime))

today = currentDateTime.strftime("%Y"+"-"+"%m"+"-"+"%d")
twoweeksleter = (currentDateTime + datetime.timedelta(days=10)).strftime("%Y"+"-"+"%m"+"-"+"%d")
print("Today'a date: {}".format(today))
print("Date 2 weeks later: {}".format(twoweeksleter))