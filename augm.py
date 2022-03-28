#augmentation script

import matplotlib.pyplot as plt
import random
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.preprocessing.image import array_to_img, img_to_array

#add noise / args: numpy array - image
def addNoise(img):
    #add random noise to an image'''
    VARIABILITY = 50
    deviation = VARIABILITY*random.random()
    noise = np.random.normal(0, deviation, img.shape)
    img += noise
    np.clip(img, 0., 255.)
    return img

#apply noise augmentation / args: numpy array - image
def noiseAugm(img):
    #data-augmenting data generator
    datagen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            zoom_range=0.2,
            preprocessing_function=addNoise,
        )
    
    #generate distorted images
    images = [img]
    img = img.reshape((1,) + img.shape)
    for batch in datagen.flow(img, batch_size=1):
        images.append( image.img_to_array(image.array_to_img(batch[0])) )
        if len(images) >= duplication:
            break   
    return images

#get augmented data / args: list - real images data, int - number of augmentation output images per image
def getAugmData(data, duplication):
    augmData={}
    for cat in data:
        augmData[cat] = []
        for i in data[cat]:
            augmImages = noiseAugm(i)
            for ai in augmImages: 
                augmData[cat].append(ai)
                print("augmentaion: " + str(len(augmImages)))
    return augmData








