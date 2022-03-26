#main script
from data import getWasteData
import matplotlib.pyplot as plt

data = getWasteData()
print(plt.imshow(data["cartons"][0]/255))






