'''
Description from the course:
    https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

    Data to used:
    We are going to use the iris flowers dataset. This dataset is famous because it is used as the “hello world”
    dataset in machine learning and statistics by pretty much everyone.
    The data will be available from a CSV file at: https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv

Here is an overview of what we are going to cover:

    0. Version check
    1. Import necessary libraries of Python
    2. Loading the dataset.
    3. Summarizing the dataset.
    4. Visualizing the dataset.
    5. Evaluating some algorithms.
    6. Making some predictions.
'''

'''
0: Version check (once checked then commented out)

#Pythos version
import sys
print('Python: {}'.format(sys.version))
#scipy version
import scipy as sp
print('scipy: {}'.format(sp.__version__))
#numpy version
import numpy as np
print('numpy: {}'.format(np.__version__))
#matplotlib version
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
#pandas version
import pandas as pd
print('pandas: {}'.format(pd.__version__))
#sklearn version
import sklearn
print('sklearn: {}'.format(sklearn.__version__))
'''
'''
1: Import necessary libraries of Python
'''
# Load libraries
import pandas as pd
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

'''
2: Loading the dataset
'''
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

'''
3: Summarizing the dataset:
    a. Dimensions of the dataset
    b. Peek at the data itself
    c. Statistical summary of all attributes
    d. Breakdown of the data by the class variable
'''
# a. Dimensions of teh dataset
#shape
print(dataset.shape)

# b. Peek at the dataset itself
#head
print(dataset.head(5))
#tail
print(dataset.tail(5))

# c. Statistical summary of all attributes
print(dataset.describe())

# d. Class distribution
print(dataset.groupby('class').size())

'''
4: Visualizing the dataset:
    a. Univariate plots to better understand each attribute
    b. Multivariate plots to better understand the relationships between attributes
'''
# a.1 Univariate plotting: box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

# a.2 Univariate plotting: histograms
dataset.hist()
pyplot.show()

# b. Multivariate plotting: scatter plot matrix
scatter_matrix(dataset)
pyplot.show()

'''
5: Evaluating some algorithms:
    a. Separate out a validation dataset.
    b. Set-up the test harness to use 10-fold cross validation.
    c. Build multiple different models to predict species from flower measurements
    d. Select the best model.
'''
# Split-out validation dataset
feature_col_names = ['sepal-length', 'sepal-width',  'petal-length',  'petal-width']
class_col_name = 'class'

# X = dataset[['sepal-length', 'sepal-width',  'petal-length',  'petal-width']].values
# y = dataset['class'].values
X = dataset[feature_col_names].values
y = dataset[class_col_name].values
split_test_size = 0.20

# array = dataset.values
# X = array[:,0:4]
# y = array[:,4]

X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=split_test_size, random_state=1)

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# Compare Algorithms
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()

'''
6. Making some predictions
	previous section suggest that the SVM was perhaps the most accurate model. We will use this model as our final model
	We'll FIT the model on the entire training dataset and make PREDICTIONS on the validation dataset
'''
# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))