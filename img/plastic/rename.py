import os
# get the file name list to nameList
nameList = os.listdir() 
#loop through the name and rename
for fileName in nameList:
    if len(fileName)>6:
        rename=fileName[7:]
        os.rename(fileName,rename)
print("done")
