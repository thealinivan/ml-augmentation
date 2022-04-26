import os
# get the file name list to nameList
nameList = os.listdir() 
#loop through the name and rename
for fileName in nameList:
    rename=fileName[9:]
    os.rename(fileName,rename)
print("done")