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
data = []
noiseAugData = []
colorAugData = []
mixedAugData = []
results = [[],[]]

#START
createWelcomeScreen()
opt = createMenu()
while opt != "0":
    
    #LOAD DATA
    if opt == "1":
        
        subOpt = createSubMenu(ACTIONS[0])
        while subOpt != "9":
            #load real images
            if subOpt == "1":
                res = int(createResolution())
                data = []
                data = loadData(FILE[0], CATEGORIES, [res, res])
                displayData(data)
    
            #load noise-augm data
            elif subOpt == "2":
               res = int(createResolution())
               noiseAugData = []
               noiseAugData = loadData(FILE[1] , CATEGORIES, [res, res])
               displayData(noiseAugData)
           
            #load color-aug data
            elif subOpt == "3":
                res = int(createResolution())
                colorAugData = []
                colorAugData = loadData(FILE[2] , CATEGORIES, [res, res])
                displayData(colorAugData)
        
            #load mixed-aug data
            elif subOpt == "4":
                res = int(createResolution())
                mixedAugData = []
                mixedAugData = loadData(FILE[3] , CATEGORIES, [res, res])
                displayData(mixedAugData)
                
            #return to main menu
            elif subOpt == "9":
                break
        
            #wrong input   
            else:
                print("Invalid option !")
        
            plt.pause(0.0001)
            subOpt = createSubMenu(ACTIONS[0])
    
    #AUGMENT DATA
    elif opt == "2":
        
        subOpt = createSubMenu(ACTIONS[1])
        while subOpt != "9":
            #apply noise
            if subOpt == "1":
                duplicates = int(createAugmNumber())
                noiseAugData = createAugmData(FILE[1], data, duplicates)
                saveData(FILE[1], noiseAugData)
                displayData(noiseAugData)
        
            #apply color
            elif subOpt == "2":
                duplicates = int(createAugmNumber())
                colorAugData = createAugmData(FILE[2], data, duplicates)
                saveData(FILE[2], colorAugData)
                displayData(colorAugData)
            
            #apply mixed (noise+color)
            elif subOpt == "3":
                duplicates = int(createAugmNumber())
                mixedAugData = createAugmData(FILE[3], data, duplicates)
                saveData(FILE[3], mixedAugData)
                displayData(mixedAugData)
                
            #return to main menu
            elif subOpt == "9":
                break
            
            #wrong input   
            else:
                print("Invalid option !")
            
            plt.pause(0.0001)
            subOpt = createSubMenu(ACTIONS[1])
    
    #DISPLAY
    elif opt == "3":
        
        subOpt = createSubMenu(ACTIONS[2])
        while subOpt != "9":
            #display current load (data)
            if subOpt == "1":
                displayData(data)
                
            #display current load (noise-augm data)
            elif subOpt == "2":
                displayData(noiseAugData)
            
            #display current load (color-aug data)
            elif subOpt == "3":
                displayData(colorAugData)
            
            #display current load (mixed (noise+color))
            elif subOpt == "4":
                displayData(mixedAugData)
                
            #return to main menu
            elif subOpt == "9":
                break
            
            #wrong input   
            else:
                print("Invalid option !")
            
            plt.pause(0.0001)
            subOpt = createSubMenu(ACTIONS[2])
    
    #MACHINE LEARNING
    elif opt == "4":
        
        subOpt = createSubMenu(ACTIONS[3])
        while subOpt != "9":
            #classifiers
            if subOpt == "1":
                print("@@@@@ KNeighrbors")
                results[0] = []
                results[0] = runML(ML[0], [data, noiseAugData, colorAugData, mixedAugData])
                displayMLResults(ML[0], results)
            #CNN
            elif subOpt == "2":
                print("@@@@@ CNN")
                results[1] = []
                results[1] = runML(ML[1], [data, noiseAugData, colorAugData, mixedAugData])
                displayMLResults(ML[1], results)
                
            #return to main menu
            elif subOpt == "9":
                break
                
            #wrong input   
            else:
                print("Invalid option !")
            
            plt.pause(0.0001)
            subOpt = createSubMenu(ACTIONS[3])
    
    #exit
    elif opt == "0":
        sys.exit("Terminated")
    
    #wrong input   
    else:
        print("Invalid option !")
    
    plt.pause(0.0001)
    opt = createMenu()
    
