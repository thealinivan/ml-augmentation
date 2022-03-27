#data source script

from keras.preprocessing.image import load_img as load 
from keras.preprocessing.image import img_to_array as toArr

#get file data / args: categories list, resolution list (x and y)
def getData(categories, res):
    wasteData={}
    for cat in categories:
        wasteData[cat] = []
        for i in range (1, 13):
            wasteData[cat].append(toArr(load('img/'+ cat +'/'+ str(i) +'.jpg', target_size=(res[0], res[1]))))
    return wasteData















