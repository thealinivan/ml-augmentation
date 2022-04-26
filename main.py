#main script

import sys
import matplotlib.pyplot as plt

from menu import createMenu
from menu import createAugmNumber
from menu import createResolution
from menu import createWelcomeScreen
from menu import createSubMenu

from data import saveData
from data import loadData
from data import displayData
from data import displayMLResults

from augm import createAugmData
from ml import runML

#INIT
#constants
CATEGORIES = ("carton", "plastic")
FILE = ("img", "noise", "color", "mixed")
ACTIONS = ("load", "augm", "display", "ml")
ML = ("knn", "cnn")
      
#data lists
allData=[]
results = [[],[]]
res = 64
duplicates = 1

#START
createWelcomeScreen()
opt = createMenu()
while opt != "0":
    #LOAD DATA
    if opt == "1":
        allData = []
        for i in range(0, len(FILE)):
            d = loadData(FILE[i], CATEGORIES, [res, res])
            allData.append(d)
            displayData(d)
    
    #AUGMENT DATA
    elif opt == "2": 
        for i in range(1, len(FILE)):
            d = createAugmData(FILE[i], allData[i], duplicates)
            allData[i] = d
            saveData(FILE[i], d)
            displayData(d)
    
    #DISPLAY DATA
    elif opt == "3": 
        for i in range(1, len(FILE)):
            displayData(allData[i])
    
    #MACHINE LEARNING
    elif opt == "4":
        subOpt = createSubMenu(ACTIONS[3])
        while subOpt != "9":
            #KNN
            if subOpt == "1":
                print("")
                print("Running KNN...")
                results[0] = []
                results[0] = runML(ML[0], allData)
                displayMLResults(results[0])
            #CNN
            elif subOpt == "2":
                print("")
                print("Runnin CNN...")
                results[1] = []
                results[1] = runML(ML[1], allData)
                displayMLResults(results[1])
            #return to main menu
            elif subOpt == "9": break  
            else: print("Invalid option !")
            plt.pause(0.0001)
            subOpt = createSubMenu(ACTIONS[3])
    #exit
    elif opt == "0": sys.exit("Terminated") 
    else: print("Invalid option !")
    plt.pause(0.0001)
    opt = createMenu()
    
