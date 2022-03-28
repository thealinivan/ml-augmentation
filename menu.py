#menu script

def showOptions():
    print("[1] Print data size")
    print("[2] Print image shape")
    print("[3] Display images")
    print("[4] Display augmented images")
    print("[0] Exit")

def getMenu():
    print ("==============")
    print ("*** ML Aug ***")
    print ("--------------")
    print("What would you like to do ?")
    showOptions()
    option = input("::")
    return option
    

