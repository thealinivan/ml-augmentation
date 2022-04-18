#machine learning script

import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

#data setup for ML / args: list of numpy arrays of images data (4) / return: list of 4 train+test lists of numpy arrays of images
def dataPreprocessing(data):
    result = data
    print("@@@@@ PreProcessing")
    print(data)
    return result

#KNeighbors ML method / args: list - train&test data / return - list of results
def KNN(data):
    result = []
    return result

# CNN ML method / args: list - train&test data / return - list of results
def CNN(data):
    result = []
    return result

#Machine Learning main method / args: string - MLType, list of lists - train&test data
def runML(MLType, data):
    data = dataPreprocessing(data)
    results = []
    for d in data: 
        if MLType == "knn": results.append(KNN(data))
        if MLType == "cnn": results.append(CNN(data))
    return results
        
        







