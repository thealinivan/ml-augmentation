#menu script

def showOptions():
    print("[1] Print array size")
    print("[2] Display single image")
    print("[3] Print image shape")
    print("[0] Exit")

def getMenu():
    print ("==============")
    print ("*** ML Aug ***")
    print ("--------------")
    print("What would you like to do ?")
    showOptions()
    option = input("::")
    return option
    

