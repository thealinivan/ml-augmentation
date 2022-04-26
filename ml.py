#machine learning script

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
#ml script

from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.utils import Bunch
from tensorflow.keras.utils import to_categorical
from keras import layers
from keras import models
from data import displayPreProcessingData

#concatenate np arrays 50%+50%
def concat(ln, src1, src2):
   ref1 = int(ln - ln/4*3)
   ref2 = int(ln/2)
   ref3 = int(ln - ln/4)
   d = np.concatenate(( src1.data[:ref1], src2.data[:ref1], src1.data[ref2:ref3],  src2.data[ref2:ref3] ))
   t = np.concatenate(( src1.target[:ref1], src2.target[:ref1], src1.target[ref2:ref3], src2.target[ref2:ref3] ))
   return Bunch(data=np.array(d), target=np.array(t))

#add np arrays 100% + 100%
def add(ln, src1, src2):
    bp = int(ln/2)
    d = np.concatenate(( src1.data[:bp], src2.data[:bp], src1.data[bp:], src2.data[bp:] ))
    t = np.concatenate(( src1.target[:bp], src2.target[:bp], src1.target[bp:], src2.target[bp:] )) 
    return Bunch(data=np.array(d), target=np.array(t))

#data setup for ML / args: list of numpy arrays of images data (4) / return: list of 4 train+test lists of numpy arrays of images
def dataPreprocessing(data):
    dataSets = []
    #real, noise, color, mixed
    for ds in data:
        dataSet = {}
        mergedData = []
        classes = []
        for cat in ds:
            for img in ds[cat]:
                mergedData.append(img)
        for i in range(0, len(mergedData)):
            if i < (len(mergedData)/2): classes.append(0)
            if i >= (len(mergedData)/2): classes.append(1)
        dataSet = Bunch(data=np.array(mergedData), target=np.array(classes))
        dataSets.append(dataSet)
   
    #hrn, hrc, hrm
    hrn = concat(len(dataSets[0].data), dataSets[0], dataSets[1])
    hrc = concat(len(dataSets[0].data),  dataSets[0], dataSets[2])
    hrm = concat(len(dataSets[0].data),  dataSets[0], dataSets[3])
    
    #ahrn, ahrc, ahrm
    ahrn = add(len(dataSets[0].data), dataSets[0], dataSets[1])
    ahrc = add(len(dataSets[0].data), dataSets[0], dataSets[2])
    ahrm = add(len(dataSets[0].data), dataSets[0], dataSets[3])
    
    dataSets += [hrn, hrc, hrm, ahrn, ahrc, ahrm]
    displayPreProcessingData(dataSets)
    return dataSets

#KNeighbors ML method / args: list - train&test data / return - list of results
def KNN(data):
    resize = 3*4*4*4*4*4*4
    results=[]
    for ds in data:
        X = (ds.data).reshape(len(ds.data), resize)
        y = ds.target
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, train_size=.8)
        print(np.shape(X_train), np.shape(X_test), len(y_train), len(y_test))
        clf = KNeighborsClassifier(3)
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)
        results.append(score)
    return results

# CNN ML method / args: list - train&test data / return - list of results
def CNN(data):
    resize = 3*4*4*4*4*4*4
    results=[]
    for ds in data:
        X = (ds.data).reshape(len(ds.data), resize)
        y = ds.target
        train_images, train_labels, test_images, test_labels = train_test_split(X, y, test_size=.2)
        
        #reshape
        train_images = train_images.reshape((4, 2, 2, 1))
        train_images = train_images.astype('float32') / 255
        test_images = test_images.reshape((2, 2, 2, 1))
        test_images = test_images.astype('float32') / 255
        train_labels = to_categorical(train_labels)
        test_labels = to_categorical(test_labels)
        model = models.Sequential()

        # adding convolutional and pooling layers
        # the data is converted into a 3D structure with more depth (64) and less width (3x3)
        model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(2, 2, 1)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        
        # Adding a classifier to the network
        # the last layers are like those of a standard ANN
        model.add(layers.Flatten())
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(10, activation='softmax'))
        model.summary()
        
        # calculating the number of parameters
        # weights in a convolutional layer: n_channels * n_kernels * kernel_size + bias
        # n_channels after 0 = kernels in previous layer (depth of network)
        weights1 = 1 * 32 * 3*3 + 32  # conv 0
        weights2 = 32 * 64 * 3*3 + 64 # conv 1
        weights3 = 64 * 64 * 3*3 + 64 # conv 2
        weights4 = 576 * 64 + 64 # dense 0
        weights5 = 64 * 10 + 10  # dense 1
        weights_tot = weights1 + weights2 + weights3 + weights4 + weights5
        #print(weights1, weights2, weights3, weights4, weights5, weights_tot)
        
        #model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
        model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.01), loss='categorical_crossentropy', metrics=['accuracy'])
        model.fit(train_images, train_labels, epochs=10, batch_size=128)
        
        test_loss, test_acc = model.evaluate(test_images, test_labels)
        results.append(test_acc)
    return results
  
#Machine Learning main method / args: string - MLType, list of lists - train&test data
def runML(MLType, data):
    data = dataPreprocessing(data)
    results = []
    if MLType == "knn": results.append(KNN(data))
    if MLType == "cnn": results.append(CNN(data))
    return results





