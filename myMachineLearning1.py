'''
Excercise from towardsdatascienece.com: on Random Forest in Python - A Practical End-to-End Machine Learning Example
Steps in ML model creation:
    State the question and determine required data
    Acquire the data in an accessible format
    Identify and correct missing data points/anomalies as required
    Prepare the data for the machine learning model
    Establish a baseline model that you aim to exceed
    Train the model on the training data
    Make predictions on the test data
    Compare predictions to the known test set targets and calculate performance metrics
    If performance is not satisfactory, adjust the model, acquire more data, or try a different modeling technique
    Interpret model and report results visually and numerically
'''
import pandas as pd
import requests
import datetime
from matplotlib import pyplot as plt

# Read in data and display first 5 rows
features = pd.read_csv('~/Desktop/Learning/DataScience/ML Exercise/temps.csv')
print(features.head(5))
print(features.info())
print(features.describe())
print(features.shape)