#main script

import sys
import matplotlib.pyplot as plt
from data import getData
from menu import getMenu

#init
CATEGORIES = ["carton", "plastic"]
data = getData(CATEGORIES, [100, 100])
    
#start
def start():
    print("")
    opt = getMenu()
    print("Response:")
    
    if opt == "1":
        print(len(data))
        
    elif opt == "2":
        print(plt.imshow(data["plastic"][7]/255))  
        
    elif opt == "3":
        print(data["plastic"][0].shape)
        
    elif opt == "0":
        sys.exit("Terminated")
        
    else:
        print("Invalid option !")
        start()
    plt.pause(0.0001)
    start()
           
#run    
start()
