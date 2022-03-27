#main script

import sys
import matplotlib.pyplot as plt
from data import getData
from menu import getMenu

#init
CATEGORIES = ("carton", "plastic")
data = getData(CATEGORIES, [100, 100])
    
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
        for cat in data:
            for i in range(0, 12):
                print(plt.imshow(data[cat][i]/255))
                plt.pause(0.001)
        
    elif opt == "3":
        print(data["plastic"][0].shape)
        
    elif opt == "4":
        print(data['plastic'][0])
        
    elif opt == "0":
        sys.exit("Terminated")
        
    else:
        print("Invalid option !")
        start()
    plt.pause(0.0001)
    start()
           
#run    
start()
