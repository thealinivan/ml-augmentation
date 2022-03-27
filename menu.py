#menu script

def showOptions():
    print("[1] Print data size")
    print("[2] Display images")
    print("[3] Print image shape")
    print("[4] Print image (np array)")
    print("[0] Exit")

def getMenu():
    print ("==============")
    print ("*** ML Aug ***")
    print ("--------------")
    print("What would you like to do ?")
    showOptions()
    option = input("::")
    return option
    

