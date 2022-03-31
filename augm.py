#augmentation script

import matplotlib.pyplot as plt
import cv2
import random
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.preprocessing.image import array_to_img, img_to_array

#add noise / args: numpy array - image
def addNoise(img):
    VARIABILITY = 50
    deviation = VARIABILITY*random.random()
    noise = np.random.normal(0, deviation, img.shape)
    img += noise
    np.clip(img, 0., 255.)
    return img

def changeColor(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

#get data generator / args: string - augmentation type / return data generation - data generation
def getDataGen(agt):
    if agt == "noise":
        datagen = ImageDataGenerator(
                preprocessing_function=addNoise,
            )
    elif agt == "color":
        datagen = ImageDataGenerator(
                rescale=1. / 255,
                rotation_range=20,
                width_shift_range=0.2,
                height_shift_range=0.2,
                horizontal_flip=True,
                preprocessing_function = changeColor,
            )
    elif agt == "mixed":
        datagen = ImageDataGenerator(
                rescale=1./255,
                rotation_range=40,
                width_shift_range=0.2,
                height_shift_range=0.2,
                zoom_range=0.2,
                preprocessing_function=addNoise,
            )
    return datagen

#get augmented data / args: string - augmentation type, list - real images data, int - number of augmentation output images per image
def createAugmData(agt, data, duplication):
    augmData={}
    for cat in data:
        augmData[cat] = []
        for img in data[cat]:
            #augmImages = noiseAugm(i, duplication)
            images = []
            img = img.reshape((1,) + img.shape)
            datagen = getDataGen(agt)
            for batch in datagen.flow(img, batch_size=1):
                images.append( image.img_to_array(image.array_to_img(batch[0])) )
                if len(images) >= duplication:
                    break  
            for ai in images: 
                augmData[cat].append(ai)
    return augmData



 
 




