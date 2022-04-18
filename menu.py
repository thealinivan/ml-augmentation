#menu script

def createWelcomeScreen():
    print("")
    print("*******************************************************************")
    print("Welcome!")
    print("This is a research of the efficiency of augmentation of data in ML")
    print("Please use the menu to perform different actions")
    print("")
    print("!!! Note that no data is pre-loaded")
    print("You can display only what you have prior loaded")
    print("*tip: Start by loading real images")
    print("*******************************************************************")

def createOptions():
    print("[1] Load Data")
    print("[2] Augment Data")
    print("[3] Display Data")
    print("[4] Apply Machine Learning")
    print("[0] Exit")
    
def createLoadOptions():
    print("[1] Load Real images")
    print("[2] Load Noise augmented images")
    print("[3] Load Color augmented images")
    print("[4] Load Mixed augmented images (noise+color")
    print("[9] Return")
    
def createAugmOptions():
    print("[1] Apply Noise augmentation")
    print("[2] Apply Color augmentation")
    print("[3] Apply mixed augmentation")
    print("[9] Return")
    
def createDisplayOptions():
    print("[1] Display Real images")
    print("[2] Display Noise augm images")
    print("[3] Display Color augm images")
    print("[4] Display Mixed augm images")
    print("[9] Return")
    
def createMLOptions():
    print("Real, Augm & Hybrids (Train & Test)")
    print("")
    print("[1] KNN")
    print("[2] CNN")
    print("[9] Return")
    
def createMenu():
    print ("==============")
    print ("*** ML Aug ***")
    print ("--------------")
    print("What would you like to do ?")
    createOptions()
    option = input("::")
    return option

def createSubMenu(opt):
    print ("--------------")
    print("What kind of action ?")
    print ("--------------")
    if opt == "load": createLoadOptions()
    elif opt == "augm": createAugmOptions()
    elif opt == "display": createDisplayOptions()
    elif opt == "ml": createMLOptions()
    option = input("::")
    return option

def createAugmNumber():
    print("How many duplicates would you like to create?")
    option = input("::")
    return option

def createResolution():
    print("Please specify resolution?")
    option = input("::")
    return option


        

