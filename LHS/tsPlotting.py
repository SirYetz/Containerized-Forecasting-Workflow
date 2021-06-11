import numpy as np
import bisect
import matplotlib.pyplot as plt
import os
import math
import matplotlib.patches as mpatches
import os, os.path
import shutil
from numpy.polynomial import Polynomial

#Amend this depending on the length of the WRF run in hours
RUN_LENGTH = 24
#print (len([name for name in os.listdir('C:\\Users\\jhmil\\tsout') ]))
xPoints = []
yPoints = []
filenames = []
directory = 'C:\\Users\\jhmil\\tsout'
directory2='C:\\Users\\jhmil\\outfiles'
for filename in os.listdir(directory):
    filenames.append(filename)
#print (filenames)
count = 0
if not os.path.exists(directory2):
            os.mkdir(directory2)
for r in filenames:
    file = 'C:\\Users\\jhmil\\tsout\\'+r
    if os.path.getsize(file)!=0:
        with open(file,'r') as f:
            lines = f.readlines()
        del lines[0]
#Writes edited file to a new file with a .out extension
    with open(file + ".out", 'w')as f:
        for line in lines:
            f.writelines(line)
    shutil.move('C:\\Users\\jhmil\\tsout\\'+r+'.out', 'C:\\Users\\jhmil\\outfiles\\'+r+'.out')
    file2 = 'C:\\Users\\jhmil\\outfiles\\'+r+'.out'
    try:
        if os.path.getsize(file2)!=0:
            file2arr = np.loadtxt(file2)
            timmy = file2arr[:,7]
            xPoints.insert(count, timmy)
            timmy = file2arr[:,8]
            yPoints.insert(count, timmy)
            count += 1
        elif os.path.getsize(file2)==0:
            os.remove(file2)
    except ValueError as ve:
        os.remove('C:\\Users\\jhmil\\tsout\\'+r)
        os.remove('C:\\Users\\jhmil\\outfiles\\'+r+'.out')
#print(len(xPoints))    

file = 'C:\\Users\\jhmil\\TS Files\\5 runs\\trit.d01_5run.TS'
#file = '/home/student/run/trit.d01.TS'
#data = '/home/student/Containerized-Forecasting-Workflow/LHS/clientdata.txt'
#reads file and delete the first irrelevant line of text
with open(file,'r') as f:
    lines = f.readlines()
del lines[0]
#Writes edited file to a new file with a .out extension
with open(file + ".out", 'w')as f:
    for line in lines:
        f.writelines(line)

file2 = 'C:\\Users\\jhmil\\TS Files\\trit.d01.TS.out'
#file2 = '/home/student/run/trit.d01.TS.out'
#loads u wind component to array
#xPoints = (np.loadtxt(file2)[:,7])

data = 'C:\\Users\\jhmil\\clientdata.txt'
#loads observed wind speed from file
clientData = (np.loadtxt(data)) 
#This is neccessary to ensure the predicted wind speed and observed have the same time steps
xWindArray =[]
#xWindArray2 =[]
yWindArray = []
#yWindArray2 = []
for r in range(len(xPoints)):
    xWindArray2 =[]
    yWindArray2 = []
    xWind = 0
    yWind = 0
    windTimeStep = 0
    windTimeStep =  RUN_LENGTH/len(xPoints[r])
    for i in range(len(xPoints[r])):
        xWindArray2.append(xWind)
        yWindArray2.append(yWind)
        xWind = xWind+windTimeStep
        yWind = yWind+windTimeStep
    #print(len(yWindArray2))
    xWindArray.insert(r, xWindArray2)
    yWindArray.insert(r, yWindArray2)
#As per previous comment
clientTimeStep = RUN_LENGTH/len(clientData)
xClient = 0
xClientArray = []
for i in range(len(clientData)):
    xClientArray.append(xClient)
    xClient = xClient+clientTimeStep
#print(len(xWindArray))
#print(xWindArray)
#print(xPoints)
#print(len(xWindArray[0]))
#print(len(yWindArray[0]))

windMagnitude = []
u = []
v = []
for i in range(len(xPoints)):
    windMagnitude2 = []
    u = xPoints[i]
    v = yPoints[i]
    for j in range(len(xPoints[i])):
        magnitude = math.sqrt(u[j]**2+v[j]**2)
        windMagnitude2.append(magnitude)
    windMagnitude.insert(i, windMagnitude2)
  
for i in range(len(xWindArray)):
    p = Polynomial.fit(xWindArray[i],windMagnitude[i],4)
    plt.plot(xWindArray[i], windMagnitude[i], 'blue')
    plt.plot(xClientArray, clientData,"red")
    plt.plot(*p.linspace(), 'cyan')
    plt.title("Wind Magnitude")
    plt.xlabel("Time (hr)")
    plt.ylabel("Wind velocity (ms-1)")
    red_patch = mpatches.Patch(color='red', label='Observed Data')
    blue_patch = mpatches.Patch(color='blue', label='Model Prediction')
    cyan_patch = mpatches.Patch(color='cyan', label='Line of Best Fit')
    plt.legend(handles=[red_patch, blue_patch, cyan_patch])
    plt.figure(i)
plt.show()