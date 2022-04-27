# ml-augmentation

Effect of augmented datasets on different machine learning algorithms in waste recycling material identification 

# Getting started

##Pre-requisites
Python 3.9.7
TensorFlow 2.8
Keras 2.8
Numpy 1.20.3
OpenCV 4.5.5


## Run on a local machine

In a terminal window
```
git clone https://labcode.mdx.ac.uk/alinivan/ml-augmentation.git
cd ml-augmentation
python main.py
```
When running a menu will appear in the terminal window as ilustrated bellow
```
*******************************************************************
Welcome!
This is a research of the efficiency of augmentation of data in ML
Please use the menu to perform different actions

!!! Note that no data is pre-loaded
You can display only what you have prior loaded
*tip: Start by loading real images
*******************************************************************
==============
*** ML Aug ***
--------------
What would you like to do ?
[1] Load Data
[2] Augment Data
[3] Display Data
[4] Apply Machine Learning
[0] Exit
```

## Program logic

**Option 1 Load Data**
 - Load real images from file (64x64 resolution)
 - Some sample images will be plotted for reference


**Option 2 - Augmunted Data**
 - Create new augmented images using the real images on a 1:1 ratio (64x64 resolution) 
 - Separate datasets are create with noise, color and both noise and color augmentation
 - Files are saved in arrays and in files
 - Some sample images will be plotted for reference

**Option 3 - Display Data**
 - Some sample images will be plotted for reference 

**Option 4 - Apply Machine Learning**
 - Will open SUBMENU
```
--------------
What kind of action ?
--------------
Real, Augm & Hybrids (Train & Test)

[1] KNN
[2] CNN
[9] Return
```
        **Sub-Option 1 - KNN**
                - Bring the images in **real**, **noise**, **color** and **mixed** datasets in pre-processing
                - Create 6 new hyrbrid data sets using **real** and **one augmentation** (3 x 50%+50% and 3 x 100% + 100%)
                - Apply K-nearest Neighbours and display the results in the terminal window
                - ML duration: 1-5 seconds


        **Sub-Option 2 - CNN**
                - Bring the images in **real**, **noise**, **color** and **mixed** datasets in pre-processing
                - Create 6 new hyrbrid data sets using **real** and **one augmentation** (3 x 50%+50% and 3 x 100% + 100%)
                - Apply Convolutional Neural Networks with 10 epochs setting and display the results in the terminal window
                - ML duration: aprox 1-2 min

Note that **every time the code is runned**, it is required to **load data** (option 1) and **augment data** (option 2) before running the machine learning processes. Altough images are saved to files, this is just for reference. The data that is used for the program logic is kept in variables until program termination.


## Files anf Folders description and requirements

**Source folder**
 - sensibile structure of folders, subfolders and python files
 - The program is reliant on .jpg image data in **img** folder, in its subfolders (carton and plastic)

**Folders:**
- img, noise, color and mixed represents the folders where the main images datasets reside
- each folder has 2 subfolders, **carton** and **plastic**
- each subfolder contains images named 0.jpg, 1.jpg etc (samples only for augmentation & more created when running the code)

**Python files:**
- main.py handles the program logic according to the selected menu options
- augm.py handles the augmentation of data
- data handles saving, loading, plotting images and displaying information in the terminal
- menu.py handles the menus and user input
- ml.py handles machine learning processes

Note each data folder contains 2 subfolders, **carton** and **plastic**. The program requires this structure to perform the logic. If these folders with their subfolders are missing please add them in the source folder before running the code.

Note the if real images are missing from the img folder (carton and plastic) the program might result in no results or errors. If not present, please add carton and plastic images in the img folder, inside each representative subfolder (carton and plastic).

## Documentation and reports
 - Project source: https://labcode.mdx.ac.uk/alinivan/ml-augmentation.git
 - Google slides result reports: https://docs.google.com/presentation/d/19AGLujYc8hrgYahQOwt9jbjkNEJsOoPbkzUiEApk0hg/edit#slide=id.p
 - Google sheets reports data source: https://docs.google.com/spreadsheets/d/1DualAXURBKLnr2EedGRYQEo90lhaAXqe3PjRa-_aBI0/edit#gid=0
 - Presentation video source: TBA

## Project info
University project
MSc Robotics
Machine Learning

## Authors and acknowledgment
Alin Ivan
Middlesex University
2022

## License
MIT


