#data source script
from keras.preprocessing.image import load_img as load 
from keras.preprocessing.image import img_to_array as toArr

def getWasteData():
    wasteData = {"plastics":[], "cartons":[]}
    for x in range (1, 13):
        wasteData["plastics"].append(toArr(load('img/plastic/1.jpg', target_size=(100, 100))))
        wasteData["cartons"].append(toArr(load('img/carton/1.jpg', target_size=(100, 100))))
    return wasteData















