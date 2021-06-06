import numpy as np
import bisect
import matplotlib.pyplot as plt
import os
import math
import matplotlib.patches as mpatches


#file = 'C:\\Users\\jhmil\\TS Files\\5 runs\\trit.d01_5run.TS'
#data = 'C:\\Users\\jhmil\\clientdata.txt'
file = '/home/student/run/trit.d01.TS'
data = '/home/student/Containerized-Forecasting-Workflow/LHS/clientdata.txt'
#reads file and delete the first irrelevant line of text
with open(file,'r') as f:
    lines = f.readlines()
del lines[0]
#Writes edited file to a new file with a .out extension
with open(file + ".out", 'w')as f:
    for line in lines:
        f.writelines(line)

#file2 = 'C:\\Users\\jhmil\\TS Files\\trit.d01.TS.out'
file2 = '/home/student/run/trit.d01.TS.out'
#loads u wind component to array
xPoints = (np.loadtxt(file2)[:,7])
#loads observed wind speed from file
clientData = (np.loadtxt(data)) 
#This is neccessary to ensure the predicted wind speed and observed have the same time steps
windTimeStep = 24/len(xPoints)
xWind = 0
xWindArray =[]
for i in range(len(xPoints)):
    xWindArray.append(xWind)
    xWind = xWind+windTimeStep
#As per previous comment
clientTimeStep = 24/len(clientData)
xClient = 0
xClientArray = []
for i in range(len(clientData)):
    xClientArray.append(xClient)
    xClient = xClient+clientTimeStep


#plot data
plt.plot(xWindArray, xPoints,"blue")
plt.plot(xClientArray, clientData,"red")
plt.title("Wind Magnitude")
plt.xlabel("Time (hr)")
plt.ylabel("Wind velocity (ms-1)")
red_patch = mpatches.Patch(color='red', label='Client Data')
blue_patch = mpatches.Patch(color='blue', label='Predicted Wind Speed')
plt.legend(handles=[red_patch, blue_patch])
plt.show()