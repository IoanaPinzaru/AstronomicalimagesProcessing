# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:03:19 2020

@author: ip1016
"""
from astropy.io import fits
import numpy as np
import math

pathic="//icnas2.cc.ic.ac.uk/ip1016/Desktop/LAB/A1/trimmed6.fits"
paththinkpad="C:/Users/User/Desktop/LAB A1/trimmed10mean.fits"
pathacer="C:/Users/Panda/Desktop/A1/trimmed10mean.fits"

hdu_list=fits.open(pathacer)
data=hdu_list[0].data
hdu_list.close()
slice=data


mean=3418.71 #background mean
sigma=11.27 #std f the background
max=10000 #initial value for the max to get the jloop going
r=6 #aperture radius
r_back=3 #annulus radius
R=r_back+r
galaxies=[] #catalogue 
list_mag=[]
count_of_errors=0

while max>mean+4*sigma: #verifying if the detected pixel exceeds the threshold
    
    #identifying the first max
    max=slice.max()
    max_arg=np.argmax(slice)+1
    max_row_y=max_arg//(slice.shape[1])+1-1
    max_col_x=max_arg%(slice.shape[1])-1
    
    #count the brightness in a circle of 6 pixels
    brightness=0
    counter=0
    for x in range(max_col_x-r,max_col_x+r):
        print(r**2-(x-max_col_x)**2)
        for y in range(int(-np.sqrt(r**2-(x-max_col_x)**2)+max_row_y)-1,int(np.sqrt(r**2-(x-max_col_x)**2)+max_row_y)+1):
            
                brightness=brightness+slice[y,x]
                counter=counter+1
                #verifica si cu patratele,Ioana
                print(y,x)
                print(slice[y,x])

    #identify the background
    counter_R=0
    brightness_R=0
    for x in range(int(max_col_x-R),int(max_col_x+R)):
        for y in range(int(-np.sqrt(R**2-(x-max_col_x)**2)+max_row_y)-1,int(np.sqrt(R**2-(x-max_col_x)**2)+max_row_y)+1):
        
                brightness_R=brightness_R+slice[y,x]
                counter_R=counter_R+1
                slice[y,x]=mean
    brightness_back=brightness_R-brightness
    counter_back=counter_R-counter
    brightness_back_average=brightness_back/counter_back
    brightness_final=brightness-brightness_back_average*counter
    
    #store the final brightness
    if brightness_final>0:
        mag=-2.5*math.log10(brightness_final)+25.3
        list=[max_row_y,max_col_x,max,brightness,brightness_back_average,brightness_final, mag]
        list_mag.append(mag)
        galaxies.append(list)
    else:
        mag=100
        count_of_errors=count_of_errors+1
        
min_mag=int(np.min(list_mag))
max_mag=int(np.max(list_mag))+1
print(galaxies)
mag_counts=[]
counter_mag=0
list_aux=[]

#count the galaxies brighter than a magnitude 
for j in range(min_mag, max_mag):
    for i in range(0,len(list_mag)):
        if list_mag[i]<j:
            counter_mag=counter_mag+1
    list_aux=[j,counter_mag]
    mag_counts.append(list_aux)
    counter_mag=0
    


import xlsxwriter

# export the data in excel
workbook = xlsxwriter.Workbook('galaxies_all_slice_new_sigma.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for i in ['y center','x center','value center','initial count','background count average','final count','mag']:
    worksheet.write(row, col,i)
    col=col+1
    
row=1
col=0

for i,j,k,l,m,n,o in galaxies:
    worksheet.write(row, col,i)
    worksheet.write(row, col+1,j)
    worksheet.write(row, col+2,k)
    worksheet.write(row, col+3,l)
    worksheet.write(row, col+4,m)
    worksheet.write(row, col+5,n)
    worksheet.write(row, col+6,o)
    row += 1

row=0
for i,j in mag_counts:
    worksheet.write(row, col+10,i)
    worksheet.write(row, col+11,j)
    row+=1
workbook.close()