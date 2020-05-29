'''
Excercise from towardsdatascienece.com: on Random Forest in Python - A Practical End-to-End Machine Learning Example
found at: https://towardsdatascience.com/random-forest-in-python-24d0893d51c0
Steps in ML model creation (Pandas dataframe approach):
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
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import export_graphviz
import pydot
from matplotlib import pyplot as plt

# Read in data and display first 5 rows
features = pd.read_csv('~/Desktop/Learning/DataScience/ML Exercise/temps.csv')
print(features.head(5))
print(features.info())
print(features.describe())
print(features.shape)
print(features['actual'])

#Data integrity check by data visualiztion
x_day = features['day']

y_Actual = features['actual']
y_Average = features['average']
y_Previousday = features['temp_1']
y_Daybeforeyesterday = features['temp_2']

# #Plot a bar graph from the data (names, runs)
# plt.figure(figsize=(20, 5))
# plt.title("Data Integrity Check")
# plt.xlabel("Days")
# plt.ylabel("Temperature")
# plt.bar(x_day,y_Average, color="Green")
# plt.grid(True)
# plt.show()

#Data cleaning and setup
#
#Repalce any NaN values to 0 in the dataset
features = features.fillna(0)

# One-hot encode the data using pandas get_dummies
features = pd.get_dummies(features, dummy_na=False)

#Display the first 5 rows of the last 12 columns print using pd.iloc[:,5:] where it will consider all rows, and columns starting at 5 to end
# print(features.iloc[:,5:].head(5))
# features.to_csv('~/Desktop/Learning/DataScience/ML Exercise/temps_after.csv')
# print(features['actual'])
''''''
# Labels are the values are kep under 'actual' column we want to predict, which is 'y'
labels = features['actual']
''''''
# Remove the label column ('actual' column) from the dataframe, we will use full df except 'actual' column as features
features= features.drop(['actual'], axis = 1)
# print(features)
# features.to_csv('~/Desktop/Learning/DataScience/ML Exercise/temps_after.csv')
# ''''''
# Saving feature names (minus 'actual') for later use, which is 'X'
feature_list = list(features.columns)
# ''''''
# Convert to numpy array
features = np.array(features)
# # print(labels)
'''
TRAINING & TESTING SETS
The following code splits the data sets with another single line:
Using Skicit-learn to split data into training and testing sets
We can also use df instead of numpy array, for more information refer to API doc: https://scikit-learn.org/stable/index.html
'''
# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)
#
#Sanity check of the shape of the data
print('Training feature data (X-training) shape = ', train_features.shape)
print('Training labels data (y-training) shape = ',train_labels.shape)
print('Test feature data (X-test) shape = ',test_features.shape)
print('Test labels data (y-test) shape = ',test_labels.shape)

'''
ESTABLISH BASELINE:
'''
# The baseline predictions are the historical averages
baseline_preds = test_features['average']
print('Baseline prediction shape = ', baseline_preds.shape)
# print('Baseline Prediction :', baseline_preds)

# Baseline errors, and display average baseline error
baseline_errors = abs(baseline_preds - test_labels)
print("The baseline average error (BAE): {} ".format(round(baseline_errors.mean(axis=0),2)))

'''
TRAIN MODEL:
After all the work of data preparation, creating and training the model is pretty simple using Scikit-learn.
We import the random forest regression model from skicit-learn, instantiate the model, and fit
'''
# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# print(rf)

# Train the model on training data
rf.fit(train_features, train_labels)

'''
MAKE PREDICTION ON THE TEST DATA:
Our model has now been trained to learn the relationships between the features and the targets.
The next step is figuring out how good the model is! To do this we make predictions on the test features (the model is 
never allowed to see the test answers). We then compare the predictions to the known answers. When performing 
regression, we need to make sure to use the absolute error because we expect some of our answers to be low and some to 
be high. We are interested in how far away our average prediction is from the actual value so we take the absolute value
(as we also did when establishing the baseline).
'''
# Use the RF's predict method on the test data
predictions = rf.predict(test_features)
# print(test_features)
# print(predictions)

# Calculate the absolute errors
errors = abs(predictions - test_labels)
# print(errors)

# Print out the mean absolute error (mae)
print('Mean Absolute Error (MAE) : {}'.format(round(errors.mean(axis=0),2)))

'''
DETERMINE PERFORMANCE METRICS:
To put our predictions in perspective, we can calculate an accuracy using
the mean average percentage error (MAPE) subtracted from 100 %
'''
# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / test_labels)
accuracy = 100 - np.mean(mape)
print('Accuracy of this model (100% - MAPE) :', round(accuracy, 2), '%.')

'''
INTERPRETATION OF 'RAIN FOREST' MODEL:
The question is: how does this model arrive at the values? 
'''
#Visualizing a Single Decision Tree (the following code will create tree of 15 levels)
# tree = rf.estimators_[5]
# export_graphviz(tree, out_file = 'tree.dot', feature_names = feature_list, rounded = True, precision = 1)
# (graph, ) = pydot.graph_from_dot_file('tree.dot')
# graph.write_png('tree.png')

#Rather create a small layered lree (3 layers)
# Limit depth of tree to 3 levels
rf_small = RandomForestRegressor(n_estimators=10, max_depth = 3)
rf_small.fit(train_features, train_labels)# Extract the small tree
tree_small = rf_small.estimators_[5]# Save the tree as a png image
export_graphviz(tree_small, out_file = 'small_tree.dot', feature_names = feature_list, rounded = True, precision = 1)
(graph, ) = pydot.graph_from_dot_file('small_tree.dot')
graph.write_png('small_tree.png')