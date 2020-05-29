'''
Description from the course:
    https://www.curiousily.com/posts/build-your-first-neural-network-with-pytorch/#data
    Title: Build Your First Neural Network with PyTorch

Objective:
    In this tutorial, we’ll build our first Neural Network using PyTorch. We’ll use it to predict whether or not is
    going to rain tomorrow using real weather information

Steps to be performed:
    - Preprocess CSV files and convert the data to Tensors
    - Build your own Neural Network model with PyTorch
    - Use a loss function and an optimizer to train your model
    - Evaluate your model and learn about the perils of imbalanced classification

Data set to be used:
    weatherAUS.csv (downloaded from: https://www.kaggle.com/jsphyg/weather-dataset-rattle-package)
'''
import numpy as np
import pandas as pd
from tqdm import tqdm
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt
from matplotlib import rc
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from torch import nn, optim
import torch.nn.functional as F
import torch

sns.set(style='whitegrid', palette='muted', font_scale=1.2)
HAPPY_COLORS_PALETTE = ["#01BEFE", "#FFDD00", "#FF7D00", "#FF006D", "#93D30C", "#8F00FF"]
sns.set_palette(sns.color_palette(HAPPY_COLORS_PALETTE))
rcParams['figure.figsize'] = 12, 8

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)

'''
DATA loading <-- start from here follow the Tutorial web

'''
df = pd.read_csv('~/Desktop/Learning/DataScience/NNExercise/weatherAUS.csv')
print(df.tail())