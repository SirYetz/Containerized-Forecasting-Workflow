"""
Author: Kieran Dineen
A little script for playing with NetCDF4 format data
This will be used to plot results of Latin Hypercube Sampling (eventually?)
"""
import numpy as np
import bisect
import matplotlib.pyplot as plt

from netCDF4 import Dataset

triton_lat=39.892
triton_long=-102

#import the nc file into a Dataset object
nc = Dataset('/home/student/run/wrfout_d01_2011-12-31_00:00:00','r')

print("The netCDF data is described as follows:\n")
print(nc)
#Print all variables
#print("Variables contained within the NetCDF file include:\n")
#print(nc.variables)

#Print info for one variable
print("\nThe variable U (x-wind component) has the following description:\n")
print(nc['U'])
print("\nU is a 32 bit float that depends on the variables Time, bottom_top, south_north and west_east_stag\n")

print(nc['PH'])
print(nc['PHB'])

#From above result we see that U is dependent on 
#Time, bottom_top, south_north and west_east_stag - 4 variables, 4 cplumns of data
uvel = nc['U'][:,:,:,:]

#The shape of the data is shown here
print("\nThe variable U the following dimensions:\n")
print(uvel.shape)

#Getting lats and longs
lats = nc['XLAT_U'][:,:,:]
longs = nc['XLONG_U'][:,:,:]

print("\nThis is how many indexes there are for lats and longs:\n")
print(lats.shape)
print(longs.shape)

#Picked indexes to get coordinates that roughly match our provided observation data
print("\nBy picking the right index we can find the coords that match our sample data:\n")
lat_index=bisect.bisect_left(lats[0,:,0],triton_lat)
long_index=bisect.bisect_left(longs[0,0,:],triton_long)
print(lats[0,lat_index,0])
print(longs[0,0,long_index])
print("\n")

#Dont really have an idea of what bottom_top variable is but just picked a number
#assuming it is vertical height but don't have an idea of the scale
#The ':' in the first position takes all U variables at the given bottom_top, lat and long
print("\nOur velocities at lat: %3.2f, long: %3.2f are:\n" % (triton_lat, triton_long))
print(uvel[:,2,lat_index,long_index])

time = nc['XTIME'][:]

xpoints = np.array(time)
ypoints = np.array(uvel[:,2,lat_index,long_index])

#plt.plot(xpoints, ypoints, 'o')
#plt.title("x-wind component at lat:%3.2f and long:%3.2f" % (triton_lat, triton_long))
#plt.xlabel("Minutes since simulation start")
#plt.ylabel("Wind velocity ms-1 (x-direction")
#plt.show()






