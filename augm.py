#augmentation script

import random
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image

#add noise / args: numpy array - image
def addNoise(img):
    VARIABILITY = 10
    deviation = VARIABILITY*random.random()
    noise = np.random.normal(0, deviation, img.shape)
    img += noise
    np.clip(img, 0., 255.)
    return img

#adapted from: https://github.com/pixelatedbrian/fortnight-furniture/blob/master/src/fancy_pca.py
# apply color augm with pca / args: numpy array - image / return: numpy array - image (0,1)
def fancy_pca(img):
    orig_img = img.astype(float).copy()
    img = img / 255.0
    img_rs = img.reshape(-1, 3)
    img_centered = img_rs - np.mean(img_rs, axis=0)
    img_cov = np.cov(img_centered, rowvar=False)
    eig_vals, eig_vecs = np.linalg.eigh(img_cov)
    sort_perm = eig_vals[::-1].argsort()
    eig_vals[::-1].sort()
    eig_vecs = eig_vecs[:, sort_perm]
    m1 = np.column_stack((eig_vecs))
    m2 = np.zeros((3, 1))
    alpha = np.random.normal(0, round(random.uniform(0.1, 0.2), 2))
    m2[:, 0] = alpha * eig_vals[:]
    add_vect = np.matrix(m1) * np.matrix(m2)
    for idx in range(3):
        orig_img[..., idx] += add_vect[idx]
    orig_img = np.clip(orig_img, 0.0, 255.0)
    orig_img = orig_img.astype(np.uint8)
    return img

# add mixed augm: noise, color, rescale, rotation angle, shift, zoom / args: numpy array - image / return numpy array - img
def mixedAug(img):
    return fancy_pca(addNoise(img))

#get data generator / args: string - augmentation type / return data generation - data generation
def getDataGen(agt):
    if agt == "noise":
        datagen = ImageDataGenerator(
                preprocessing_function=addNoise,
            )
    elif agt == "color":
        datagen = ImageDataGenerator(
                brightness_range = [0.3, 1.5],
                preprocessing_function = fancy_pca,
            )
    elif agt == "mixed":
        datagen = ImageDataGenerator(
                rescale=1./255,
                rotation_range=20,
                width_shift_range=0.1,
                height_shift_range=0.1,
                zoom_range=0.1,
                preprocessing_function=mixedAug,
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





 
 




