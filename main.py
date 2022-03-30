#main script

import sys
import matplotlib.pyplot as plt

from menu import createMenu
from menu import createAugmNumber
from menu import createResolution
from menu import createWelcomeScreen

from data import saveData
from data import loadData
from data import displayData

from augm import createAugmData


#init
CATEGORIES = ("carton", "plastic")
FILE = ("img", "noise", "color")
data = []
noiseAugData = []

createWelcomeScreen()
opt = createMenu()

while opt != "0":
    
    #load data
    if opt == "1":
        res = int(createResolution())
        data = []
        data = loadData(FILE[0], CATEGORIES, [res, res])
        displayData(data)
        
    #apply noise
    elif opt == "2":
        duplicates = int(createAugmNumber())
        noiseAugData = createAugmData(FILE[1], data, duplicates)
        saveData(FILE[1], noiseAugData)
        displayData(noiseAugData)
        
    #load noise-augm data
    elif opt == "3":
       res = int(createResolution())
       noiseAugData = []
       noiseAugData = loadData(FILE[1] , CATEGORIES, [res, res])
       displayData(noiseAugData)
       
    #display current load (data)
    elif opt == "4":
        displayData(data)
            
    #display current load (noise-augm data)
    elif opt == "5":
        displayData(noiseAugData)
    
    #exit
    elif opt == "0":
        sys.exit("Terminated")
    
    #wrong input   
    else:
        print("Invalid option !")
    
    plt.pause(0.0001)
    opt = createMenu()
    
