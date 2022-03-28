#main script

import sys
import matplotlib.pyplot as plt
from data import getData
from menu import getMenu
from augm import getAugmData

#init
CATEGORIES = ("carton", "plastic")
data = getData(CATEGORIES, [100, 100])
augData = getAugmData(data, 4)
    
#start
def start():
    print("")
    opt = getMenu()
    print("response:")
    
    if opt == "1":
        print("data size: " + str(len(data)))
        for cat in data:
            print(cat + " size: " + str(len(data[cat])))
        
    elif opt == "2":
        print(data["plastic"][0].shape)
        
    elif opt == "3":
        for cat in data:
            for i in augData[cat]:
                print(plt.imshow(i/255))
                plt.pause(0.001)
        
    elif opt == "4":
        for cat in augData:
            for i in augData[cat]:
                print(plt.imshow(i/255))
                plt.pause(0.001)
        
    elif opt == "0":
        sys.exit("Terminated")
        
    else:
        print("Invalid option !")
        start()
    plt.pause(0.0001)
    start()
           
#run    
start()
