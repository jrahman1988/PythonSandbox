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
from sklearn.impute import SimpleImputer
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
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
# print(df.head(5))
# print(df.tail(5))
# print(df.info())
# print(df.describe())
# print(df.shape)

'''
CHECK DATA:
If there is any null values in the data
'''
print("Is there any null value in the data :", df.isnull().values.any())

'''
DATA PREP 1: CLEAN UP DATA BY CORRELATION CHECK BETWEEN COLUMNS:
1. By plotting correlation map of matplotlib library (we have to use the debugger mode to see the corr df)
2. Remove the 'skin' column because it has 1 to 1 correlation with 'thickness'
'''
corr = df.corr()
# print(corr)
del df['skin']
# print(df.info())
# corr = df.corr()
# print(corr)

'''
DATA PREP 2: CLEAN UP DATA BY MOLDING DATA:
1. We have categorical data under 'diabetes' column and those are 'True' and 'False', change them to '1' and '0'
2. Use map() method of Pandas to convert 'True' to 1 and 'False' to 0 under 'diabetes' column
'''
# print(df.head())
diabetes_map = {True: 1, False: 0}
df['diabetes'] = df['diabetes'].map(diabetes_map)
# print(df.head())

'''
DATA PREP 3: CHECK THE TARGET COLUMN WHETHER IT HAS SUFFICIENT DISTRIBUTION OF TRUE/FALSE
1. Find the number of 'True' and 'False' under 'diabetes' column
'''
num_true = len(df.loc[df['diabetes'] == True])
num_false = len(df.loc[df['diabetes'] == False])
percent_numTrue:float = round((num_true/(num_true+num_false)) *100, 2)
percent_numFalse:float = round((num_false/(num_true+num_false)) *100, 2)
# print("Number of True cases: {0} - % of True = {1}".format(num_true, percent_numTrue))
# print("Number of False cases: {0} - % of False = {1}".format(num_false, percent_numFalse))

'''
TRAINING - DATA SPLITTING:
1. Using scikit-learn library split prepared data into 70% Training set and 30% Testing set
2. Define the feature set using all column names and predicted name using the diabetes column
3. Verify predicted value was split correctly
4. Check how many and what percentage of data have been splitted into Training and Teat subset
'''
feature_col_names = {'num_preg', 'glucose_conc', 'diastolic_bp', 'thickness', 'insulin', 'bmi', 'diab_pred', 'age'}
predicted_class_name = {'diabetes'}

X = df[feature_col_names].values
y = df[predicted_class_name].values
split_test_size = 0.30

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_test_size, random_state=42)
print("% of training set {}".format(round(float((len(X_train)/len(df.index))*100),2)))
print("% of test set {}".format(round(float((len(X_test)/len(df.index))*100),2)))
print("")

originalCountsTrue = len(df.loc[df['diabetes'] == 1])
originalCountsFalse = len(df.loc[df['diabetes'] == 0])

originalCountsTruePercent = round((originalCountsTrue/(originalCountsTrue+originalCountsFalse) * 100), 2)
originalCountsFalsePercent = round((originalCountsFalse/(originalCountsTrue+originalCountsFalse) * 100), 2)

print("Original True counts: {0}, ({1}%)".format(originalCountsTrue, originalCountsTruePercent))
print("Original False counts: {0}, ({1}%)".format(originalCountsFalse, originalCountsFalsePercent))
print("")

trainCountsTrue = len(y_train[y_train[:] == 1])
trainCountsFalse = len(y_train[y_train[:] == 0])

trainCountsTruePercent = round((trainCountsTrue/(trainCountsTrue+trainCountsFalse) * 100), 2)
trainCountsFalsePercent = round((trainCountsFalse/(trainCountsTrue+trainCountsFalse) * 100), 2)

print("Training True counts: {0}, ({1}%)".format(trainCountsTrue, trainCountsTruePercent))
print("Training False counts: {0}, ({1}%)".format(trainCountsFalse, trainCountsFalsePercent))
print("")

testCountsTrue = len(y_test[y_test[:] == 1])
testCountsFalse = len(y_test[y_test[:] == 0])

testCountsTruePercent = round((testCountsTrue/(testCountsTrue+testCountsFalse) * 100), 2)
testCountsFalsePercent = round((testCountsFalse/(testCountsTrue+testCountsFalse) * 100), 2)

print("Test True counts: {0}, ({1}%)".format(testCountsTrue, testCountsTruePercent))
print("Test False counts: {0}, ({1}%)".format(testCountsFalse, testCountsFalsePercent))
print("")

'''
POST-SPLIT DATA INTEGRITY CHECK/PREPARATION:
1. Check if there is any missing data (0) in any of the columns (X features)
2. Find how many rows have unexpected 0 values
'''
print(df.info())
print(df.head())
print("# of rows in the dataframe: {0}".format(len(df)))
print("# of missing data in column glucose_conc: {0}".format(len(df.loc[df['glucose_conc'] == 0])))
print("# of missing data in column diastolic_bp: {0}".format(len(df.loc[df['diastolic_bp'] == 0])))
print("# of missing data in column thickness: {0}".format(len(df.loc[df['thickness'] == 0])))
print("# of missing data in column insulin: {0}".format(len(df.loc[df['insulin'] == 0])))
print("# of missing data in column bmi: {0}".format(len(df.loc[df['bmi'] == 0])))
print("# of missing data in column diab_pred: {0}".format(len(df.loc[df['diab_pred'] == 0])))
print("# of missing data in column age: {0}".format(len(df.loc[df['age'] == 0])))

'''
IMPUTING OPERATION TO REPLACE MISSING DATA CELLS:
1. We'll use SimpleImputer class of sklearn.impute library
2. We'll Impute with mean value of all 0 readings in all columns of X_train and X_test
3. We'll use fit_transform() method of SimpleImputer class to fill in with mean and transform
'''
fill_0 = SimpleImputer(missing_values=0, strategy='mean')
X_train = fill_0.fit_transform(X_train)
X_test = fill_0.fit_transform(X_test)

'''
TRAINING OF NAIVE BAYES MODEL:
1. We'll use GaussianNB class of sklearn.naive_bayes and train with X_train y_train data
'''
nb_model = GaussianNB()
nb_model.fit(X_train, y_train.ravel())

'''
PERFORMANCE ON TRAINING DATA USING NAIVE BAYES MODEL:
1. Predict the value with X_train data
2. We need to check the prediction accuracy using training data on the Naive Bayes model
'''
nb_predict_train = nb_model.predict(X_train)
predict_performance_train = metrics.accuracy_score(y_train, nb_predict_train)
print("Accuracy of prediction with training data {0:.4f}".format(predict_performance_train))

'''
PERFORMANCE ON TESTING DATA USING NAIVE BAYES MODEL:
1. Predict the value with X_test data
2. We need to check the prediction accuracy using testing data on the Naive Bayes model
'''
nb_predict_test = nb_model.predict(X_test)
predict_performance_test = metrics.accuracy_score(y_test, nb_predict_test)
print("Accuracy of prediction with testing data {0:.4f}".format(predict_performance_test))

'''
PERFORMANCE STATISTICS MEASURE BY CONFUSION MATRIX of y_test and nb_predict_test data:
1. Using confusion_matrix() method of metrics class from sklearn library
2. Confusion matrix is to evaluate the accuracy of a classification
3. By definition a confusion matrix 'C' is such that 'Cij' is equal to the number of observations known to be in group
   'i' and predicted to be in group 'j'.
4. Thus in binary classification, the count of true negatives (TN) is 'C00', false negatives (FN) is 'C10',
    true positives (TP) is 'C11' and false positives (FP) is 'C01':
   Predicted False  Predicted True
   c00 (TN)         c01 (FP) (row = actual fasle)
   c10 (FN)         c11 (TP) (row = actual true)
5. In a perfect classifier, the matrics will be:
   c01 (FP) and c10 (FN) should be '0'
'''
print("Confusion Matrix")
print("{}".format(metrics.confusion_matrix(y_test, nb_predict_test)))
print("")

print("Classification Report")
print(metrics.classification_report(y_test, nb_predict_test))

'''
RANDOM FOREST MODEL TO IMPROVE THE PREDICTION:
1. If the Confusion matrix shows the naive bayes model needs improvement, we can try to see how Random Forest works
2. We create a RF model and train with X_train and y_train data
2. Note that, we use np.ravel() format for y_train to flatten the array
'''
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train.ravel())

rf_predict_train = rf_model.predict(X_train)
print("Training data accuracy with Random Forest model: {0:.4f}".format(metrics.accuracy_score(y_train, rf_predict_train)))

rf_predict_test = rf_model.predict(X_test)
print("Test data accuracy with Random Forest model: {0:.4f}".format(metrics.accuracy_score(y_test, rf_predict_test)))

print("Confusion Matrix with RF model")
print("{}".format(metrics.confusion_matrix(y_test, rf_predict_test)))
print("")

print("Classification Report with RF model")
print(metrics.classification_report(y_test, rf_predict_test))


