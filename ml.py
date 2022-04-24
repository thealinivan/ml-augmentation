#machine learning script

import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn import datasets

#data setup for ML / args: list of numpy arrays of images data (4) / return: list of 4 train+test lists of numpy arrays of images
def dataPreprocessing(data):
    result = data
    print("@@@@@ PreProcessing")
    print(data)
    return result

#KNeighbors ML method / args: list - train&test data / return - list of results
def KNN(data):
    classifiers = [
        KNeighborsClassifier(3),
        SVC(kernel="linear", C=0.025),
        SVC(gamma=2, C=1),
        GaussianProcessClassifier(1.0 * RBF(1.0)),
        DecisionTreeClassifier(max_depth=5),
        RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
        MLPClassifier(alpha=1, max_iter=1000),
        AdaBoostClassifier(),
        GaussianNB(),
        QuadraticDiscriminantAnalysis()]
    
    names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
             "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
             "Naive Bayes", "QDA"]
    
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    
    #X = StandardScaler().fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.4)#, random_state=42)
    
    for name, clf in zip(names, classifiers):
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)
        print(name, score)

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

KNN(1)







