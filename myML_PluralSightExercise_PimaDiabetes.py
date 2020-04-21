'''
Description from the course:
    https://app.pluralsight.com/library/courses/python-understanding-machine-learning/description
    Hello! My name is Jerry Kurata, and welcome to Understanding Machine Learning with Python.
    In this course, you will gain an understanding of how to perform Machine Learning with Python.
    You will get there by covering major topics like how to format your problem to be solvable,
    how to prepare your data for use in a prediction, and how to combine that data with algorithms to create models that can
    predict the future. By the end of this course, you will be able to use Python and the scikit-learn library to create
    Machine Learning solutions. And you will understand how to evaluate and improve the performance of the solutions you
    create. Before you begin, make sure you are already familiar with software development and basic statistics. However,
    your software experience does not have to be in Python, since you will learn the basics in this course. When you use
    Python together with scikit-learn, you will see why this is the preferred development environment for many
    Machine Learning practitioners. You will do all the demos using the Jupyter Notebook environment. This environment
    combines live code with narrative text to create a document with can be executed and presented as a web page.
    I hope you’ll join me, and I look forward to helping you on your learning journey here at Pluralsight.

ML workflow (data used from UCI ML repository):
    1. Asking the right question about what to predict or calssify
    2. Preparing the data:
        a. Find the data we need
        b. Inspect and clean the data
        c. Explore the data
        d. Mold the data to 'Tidy' data
    3. Selecting the algorithm
    4. Training the model
    5. Testing the model
'''
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import export_graphviz
import pydot
from matplotlib import pyplot as plt

#A global variable from where the dataset will be loaded
datatobeloaded = "~/Desktop/Learning/Sandbox/MLSandbox/pima-data.csv"

'''
LOADING DATA:
(pima-data.csv, which was downloaded form Jerry's GitHub repo and now saved at: ~/Desktop/Learning/Sandbox/MLSandbox
'''
df = pd.read_csv(datatobeloaded)
print(df.head(5))
print(df.tail(5))
print(df.info())
print(df.describe())
print(df.shape)

# # #Data integrity check by data visualiztion
# # x_day = features['day']
# #
# # y_Actual = features['actual']
# # y_Average = features['average']
# # y_Previousday = features['temp_1']
# # y_Daybeforeyesterday = features['temp_2']
#
# # #Plot a bar graph from the data (names, runs)
# # plt.figure(figsize=(20, 5))
# # plt.title("Data Integrity Check")
# # plt.xlabel("Days")
# # plt.ylabel("Temperature")
# # plt.bar(x_day,y_Average, color="Green")
# # plt.grid(True)
# # plt.show()
#
# #Data cleaning and setup
# #
# #Repalce any NaN values to 0 in the dataset
# features = features.fillna(0)
#
# # One-hot encode the data using pandas get_dummies
# features = pd.get_dummies(features, dummy_na=False)
#
# #Display the first 5 rows of the last 12 columns print using pd.iloc[:,5:] where it will consider all rows, and columns starting at 5 to end
# # print(features.iloc[:,5:].head(5))
# # features.to_csv('~/Desktop/Learning/DataScience/ML Exercise/temps_after.csv')
# # print(features['actual'])
# ''''''
# # Labels are the values are kep under 'actual' column we want to predict, which is 'y'
# labels = features['actual']
# ''''''
# # Remove the label column ('actual' column) from the dataframe, we will use full df except 'actual' column as features
# features= features.drop(['actual'], axis = 1)
# # print(features)
# # features.to_csv('~/Desktop/Learning/DataScience/ML Exercise/temps_after.csv')
# # ''''''
# # Saving feature names (minus 'actual') for later use, which is 'X'
# feature_list = list(features.columns)
# # ''''''
# # # Convert to numpy array
# # features = np.array(features)
# # # print(labels)
# '''
# TRAINING & TESTING SETS
# The following code splits the data sets with another single line:
# Using Skicit-learn to split data into training and testing sets
# We can also use df instead of numpy array, for more information refer to API doc: https://scikit-learn.org/stable/index.html
# '''
# # Split the data into training and testing sets
# train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)
# #
# #Sanity check of the shape of the data
# print('Training feature data (X-training) shape = ', train_features.shape)
# print('Training labels data (y-training) shape = ',train_labels.shape)
# print('Test feature data (X-test) shape = ',test_features.shape)
# print('Test labels data (y-test) shape = ',test_labels.shape)
# # print(test_features.info())
#
# '''
# ESTABLISH BASELINE:
# '''
# # The baseline predictions are the historical averages
# baseline_preds = test_features['average']
# print('Baseline prediction shape = ', baseline_preds.shape)
# # print('Baseline Prediction :', baseline_preds)
#
# # Baseline errors, and display average baseline error
# baseline_errors = abs(baseline_preds - test_labels)
# print("The baseline average error (BAE): {} ".format(round(baseline_errors.mean(axis=0),2)))
#
# '''
# TRAIN MODEL:
# After all the work of data preparation, creating and training the model is pretty simple using Scikit-learn.
# We import the random forest regression model from skicit-learn, instantiate the model, and fit
# '''
# # Instantiate model with 1000 decision trees
# rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# # print(rf)
#
# # Train the model on training data
# rf.fit(train_features, train_labels)
#
# '''
# MAKE PREDICTION ON THE TEST DATA:
# Our model has now been trained to learn the relationships between the features and the targets.
# The next step is figuring out how good the model is! To do this we make predictions on the test features (the model is
# never allowed to see the test answers). We then compare the predictions to the known answers. When performing
# regression, we need to make sure to use the absolute error because we expect some of our answers to be low and some to
# be high. We are interested in how far away our average prediction is from the actual value so we take the absolute value
# (as we also did when establishing the baseline).
# '''
# # Use the RF's predict method on the test data
# predictions = rf.predict(test_features)
# # print(test_features)
# # print(predictions)
#
# # Calculate the absolute errors
# errors = abs(predictions - test_labels)
# # print(errors)
#
# # Print out the mean absolute error (mae)
# print('Mean Absolute Error (MAE) : {}'.format(round(errors.mean(axis=0),2)))
#
# '''
# DETERMINE PERFORMANCE METRICS:
# To put our predictions in perspective, we can calculate an accuracy using
# the mean average percentage error (MAPE) subtracted from 100 %
# '''
# # Calculate mean absolute percentage error (MAPE)
# mape = 100 * (errors / test_labels)
# accuracy = 100 - np.mean(mape)
# print('Accuracy of this model (100% - MAPE) :', round(accuracy, 2), '%.')
#
# '''
# INTERPRETATION OF 'RAIN FOREST' MODEL:
# The question is: how does this model arrive at the values?
# '''
# #Visualizing a Single Decision Tree (the following code will create tree of 15 levels)
# # tree = rf.estimators_[5]
# # export_graphviz(tree, out_file = 'tree.dot', feature_names = feature_list, rounded = True, precision = 1)
# # (graph, ) = pydot.graph_from_dot_file('tree.dot')
# # graph.write_png('tree.png')
#
# #Rather create a small layered lree (3 layers)
# # Limit depth of tree to 3 levels
# rf_small = RandomForestRegressor(n_estimators=10, max_depth = 3)
# rf_small.fit(train_features, train_labels)# Extract the small tree
# tree_small = rf_small.estimators_[5]# Save the tree as a png image
# export_graphviz(tree_small, out_file = 'small_tree.dot', feature_names = feature_list, rounded = True, precision = 1)
# (graph, ) = pydot.graph_from_dot_file('small_tree.dot')
# graph.write_png('small_tree.png')