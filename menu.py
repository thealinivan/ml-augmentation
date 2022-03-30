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
    print("[1] Load real images")
    print("[2] Apply noise to real images & save augmented data")
    print("[3] Load noise-augm images")
    print("[4] Display real images (current load)")
    print("[5] Display noise-augm images (current load)")
    print("[0] Exit")

def createMenu():
    print ("==============")
    print ("*** ML Aug ***")
    print ("--------------")
    print("What would you like to do ?")
    createOptions()
    option = input("::")
    return option

def createAugmNumber():
    print("How many duplicates would you like to create? 1 to 10 advised for dev")
    option = input("::")
    return option

def createResolution():
    print("Please specify resolution? multiples of 10 (40, 120, 270)")
    option = input("::")
    return option


        

