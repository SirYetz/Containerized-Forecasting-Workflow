import numpy as np
import bisect
import matplotlib.pyplot as plt
import os
import math


file = 'C:\\Users\\jhmil\\trit.d01.TS'
data = 'C:\\Users\\jhmil\\clientdata.txt'
#file = '/home/student/run/trit.d01.TS'
#reads file and delete the first irrelevant line of text
with open(file,'r') as f:
    lines = f.readlines()
del lines[0]
#Writes edited file to a new file with a .out extension
with open(file + ".out", 'w')as f:
    for line in lines:
        f.writelines(line)

file2 = 'C:\\Users\\jhmil\\trit.d01.TS.out'
#file2 = '/home/student/run/trit.d01.TS.out'
#loads u wind component to array
xPoints = (np.loadtxt(file2)[:,7])
#loads v wind componenet to array
yPoints = (np.loadtxt(file2)[:,8])
#Create array which will be used to store magnitude of wind
windMagnitude = []
#Create array which acts as a coutner to track time steps
timeStep = []
clientData = (np.loadtxt(data))
#parse arrays of u and v components to determine true magnitude of wind speed 
for i in range(len(xPoints)):
    u = xPoints[i]
    v = yPoints[i]
    magnitude = math.sqrt(u**2+v**2)
    windMagnitude.append(magnitude)
    #timeStep.append(i)
windTimeStep = 24/len(windMagnitude)
xWind = 0
xWindArray =[]
for i in range(len(windMagnitude)):
    xWindArray.append(xWind)
    xWind = xWind+windTimeStep
clientTimeStep = 24/len(clientData)
xClient = 0
xClientArray = []
for i in range(len(clientData)):
    xClientArray.append(xClient)
    xClient = xClient+clientTimeStep
#print(xClientArray)
#print(xWindArray)
#print(xWind)
#print(xClient)
#print (windMagnitude)
#print (timeStep)
#print(clientData)

#plot data
plt.plot(xWindArray, windMagnitude)
plt.plot(xClientArray, clientData)
plt.title("Wind Magnitude")
plt.xlabel("Time Step")
plt.ylabel("Wind velocity ms-1")
plt.show()