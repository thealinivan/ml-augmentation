#data source script
import cv2
from keras.preprocessing.image import load_img as load 
from keras.preprocessing.image import img_to_array as toArr
import matplotlib.pyplot as plt
import numpy as np

headings = [
     "real:  ",
     "noise: ",
     "color: ",
     "mixed: ", 
     "hrn:   ",
     "hrc:   ",
     "hrm:   ",
     "ahrn:  ",
     "ahrc:  ",
     "ahrm:  ",
     ]

#get file data / args: string - file, categories list, resolution list (x and y) / return: object - images
def loadData(file, categories, res):
    data={}
    iterator = 0
    for cat in categories:
        iterator = 0
        data[cat] = []
        for i in range(0, 1000):
            try:
                el = toArr(load(file + '/'+ cat +'/'+ str(i) +'.jpg', target_size=(res[0], res[1])))
                data[cat].append(el)
            except IOError: break
        iterator += 1
    return data
    
#display data / args: array - images
def displayData(dataType, data):
    #for cat in data:
        #for i in data[cat]:
           #print(plt.imshow(i/255))
            #plt.pause(0.001)
    print("")
    print(dataType + " data...")
    print("data size: " + str(len(data)))
    for cat in data:
        print(cat + " size: " + str(len(data[cat])))
    

def displayMLResults(results):
    print("")
    print("Results...")
    names = headings
    for name, score in zip(names, results[0]):
        print(name, score)

def displayPreProcessingData(dataSets):
    print("")
    print("Pre-Processing Data...")
    names = headings
    for name, ds in zip(names, dataSets):
        print(name + "data " + str(len(ds.data)) + "   target " + str(len(ds.data)))
    
#save augmented data / args: string - augmentation type
def saveData(file, data):
    iterator = 0
    for cat in data:
        iterator = 0
        for i in data[cat]:
            cv2.imwrite(file + "/" + cat + '/' + str(iterator) + '.jpg', i)
            iterator += 1
            
        