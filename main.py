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

from augm import createAugmData


#INIT
#constants
CATEGORIES = ("carton", "plastic")
FILE = ("img", "noise", "color")
ACTIONS = ("load", "augm", "display", "ml")
#data lists
data = []
noiseAugData = []
colorAugData = []

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
                print("#load mixed-aug")
                
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
                print("#augm mixed")
                
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
                print("#load mixed")
                
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
            #train real
            if subOpt == "1":
                print("#ML train real")
            #test real
            elif subOpt == "2":
                print("#ML test real")
            
            #train +noise
            elif subOpt == "3":
                print("#ML train +noise")
            #test +noise
            elif subOpt == "4":
                print("#ML test +noise")
            
            #train +color
            elif subOpt == "5":
                print("#ML train +color")
            #test +color
            elif subOpt == "6":
                print("#ML test +color")
            
            #train +mixed
            elif subOpt == "7":
                print("#ML train +mixed")
            #test +mixed
            elif subOpt == "8":
                print("#ML test +mixed")
                
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
    
